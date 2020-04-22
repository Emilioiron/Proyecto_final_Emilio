import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.preprocessing import RobustScaler
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# Cargo el modelo a utilizar
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV


# 1. Data Loading

bomba_data = pd.read_csv('data/processed/Data.csv')

# 2. EDA (Exploratory Data Analysis)
# In jupyter notebook

# 3. ML PREPROCESSING

# Food estimate lo quitamos de la lista por correlación = 1 con BWZ Estimate (U)
# Divido las columnas en númericas y categóricas
# Indico la columna objetivo y = TARGET

NUM_FEATS = ['Basal Rate (U/h)','BWZ Carb Ratio (U/Ex)','BWZ Insulin Sensitivity (mg/dL/U)',
             'BWZ Carb Input (exchanges)', 'BWZ BG Input (mg/dL)','BWZ Correction Estimate (U)',
             'BWZ Active Insulin (U)','BWZ Unabsorbed Insulin Total (U)']
CAT_FEATS = ['day_of_month', 'day_of_week', 'month_of_year', 'hour']
FEATS = NUM_FEATS + CAT_FEATS
TARGET = 'BWZ Estimate (U)'

# Preprocessing...
# Defino el Pipelinte de las columnas numéricas
numeric_transformer = \
Pipeline(steps=[('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())])

# Defino el Pipelinte de las columnas categóricas
categorical_transformer = \
Pipeline(steps=[('imputer', SimpleImputer(strategy='constant',fill_value=-999999)),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, NUM_FEATS),
                                              ('cat', categorical_transformer, CAT_FEATS)])

# Paso a DataFrame los datos procesados
pd.DataFrame(data=preprocessor.fit_transform(bomba_data))

# Al haber muchas columnas nuevas categóricas se crea una única columna comprimida que sirve igualmente para realizar todo el proceso.
data=preprocessor.fit_transform(bomba_data)

# Se definen X_train, X_test, y_train, y_test a partir de bomba_data.
X_train, X_test, y_train, y_test = train_test_split(bomba_data[FEATS], bomba_data[TARGET], test_size=0.2)

# Verifico las dimensiones de X_train, X_test, y_train, y_test
print('Verificando las dimensiones de X_train, X_test, y_train, y_test')
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Defino el modelo y los pasos (steps) a utilizar en el Pipeline
model= Pipeline(steps=[('preprocessor', preprocessor),
                       ('regressor', RandomForestRegressor())])

# Entreno el modelo
model.fit(X_train, y_train);

# 5. Check model performance on test and train data

# Defino los datos sobre los que se va a predecir en el modelo X_train y X_test
# Nota: En el Pipeline de categorical_transformer hay que poner fill_value=-999999
# para que no de un error de falta de datos en alguna celda debido a la transformación

y_predict_train = model.predict(X_train)
y_predict_test = model.predict(X_test)

#Error sobre train y sobre test

print(f"train error: {mean_squared_error(y_pred=y_predict_train, y_true=y_train, squared=False)}")
print(f"test error: {mean_squared_error(y_pred=y_predict_test, y_true=y_test, squared=False)}")

# Calculo del error metrica r2_score

print(f' test train: {r2_score(y_true=y_train, y_pred=y_predict_train)}')
print(f' test error: {r2_score(y_true=y_test, y_pred=y_predict_test)}')

# 6. Check model performance using cross validation

scores = cross_val_score(model,
                         bomba_data[FEATS],
                         bomba_data[TARGET],
                         scoring='neg_root_mean_squared_error',
                         cv=32, n_jobs=-1)


import numpy as np
np.mean(-scores)
print(-scores)


# 7. Optimize model using grid search
# Se definen los parametros del grid y del model
# verbose muestra los pasos que ha haciendo el modelo de entrenamiento.
# cv : validación cruzada
# n_jobs = -1 significa que utiliza todos los procesadores para realizar el proceso.
#
param_grid = {
    'preprocessor__num__imputer__strategy': ['mean', 'median','most_frequent','constant'],
    'regressor__n_estimators': [8,16,64,128,256,512],
    'regressor__max_depth': [4,8,16,32],
    'regressor__max_features': ['auto', 'sqrt']
}

grid_search = RandomizedSearchCV(model,
                                 param_grid,
                                 cv= 10,
                                 verbose=10,
                                 scoring='neg_root_mean_squared_error',
                                 n_jobs=-1,
                                 n_iter=8)

grid_search.fit(bomba_data[FEATS], bomba_data[TARGET])

# Visualizo los mejores parámetros
grid_search.best_params_
grid_search.best_score_
grid_search.best_estimator_.score

y_test = pd.DataFrame(y_test)

y_test.to_csv('data/results/Results_y_test.csv')


#import pickle
#pickle.dumps(model, open('data/results/model.pkl', 'wb'))

from sklearn.externals import joblib
joblib.dump(model, 'data/results/model.pkl')




