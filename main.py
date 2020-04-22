import pandas as pd
import numpy as np
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

title_graphic = input('Enter the title: ')
mac.acquire()
Data = mwr.wrangle()
by_hour_mean= mre.data_by_hour(Data)
#by_day_of_week_mean = mre.data_by_week(Data)
#mre.plotting_function(by_hour_mean,by_day_of_week_mean, title_graphic)

#model_pickle = pickle.loads(open('data/results/model.p', 'rb'))
#new_food = pd.read_csv('data/results/New_data.csv')
#administrar_insulina= model_pickle.predict(new_food)

from sklearn.externals import joblib
model_pickle = joblib.load('data/results/model.pkl')
new_food = pd.read_csv('data/results/New_data.csv')
administrar_insulina = model_pickle.predict(new_food)
pd.DataFrame(administrar_insulina).to_csv('data/results/administrar_insulina.csv')
print(f'Te debes administrar ' + pd.DataFrame(administrar_insulina).iloc[0,0].round(2).astype(str) + ' unidades de insulina')


if __name__ == '__main__':
    print('Pipeline successfully completed')





# Nota: Hay que escribir algo debajo de __main__ si no no funciona bien


