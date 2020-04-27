
![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)




# Modelo de machine learning para predecir la inyección de insulina de un diabético

Proyecto final Ironhack

## Objetive

* El Objetivo de este proyecto es crear un modelo de Machine Learning que prediga la insulina que tiene que inyectarse un diabético tipo I a partir de los datos que se obtienen de la persona a partir de su bomba de insulina.

## Needs

* Dependiendo de los Hidratos de Carbono que una persona come, el pancreas suministra más o menos insulina de forma inmediata. A los diabeticos tipo-1 no les funciona el pancreas y necesitan inyectarse insulina cada vez que comen. 

* Es complicado ajustar la insulina a lo que come una persona diabética en cada momento y esto es un problema muchas veces para ellos ya que pueden tener niveles muy altos o muy bajos de glucosa en sangre debido a un cálculo erroneo y esto puede desencadenar en problemas de salud graves o incluso la muerte, a largo plazo.

* Este modelo calcula las unidades de insulina que un diabético necesita según lo que come a partir de los parámetros que tiene su bomba de insulina (personalizados), hora y día de la semana.



## Steps I have followed

* Se crea un repositirio para el proyecto con el nombre de "Proyecto_final_Emilio".
* Descargar los datos de la bomba de insulina (Medtronic) desde su aplicación Carelink.
* Se descargan los datos desde junio de 2015 hasta marzo de 2020.
* Los datos no se pueden descargar de forma personalizada con fecha de inicio y fin para más de tres meses, por lo que hay que descargar 20 archivos en formato CSV para después unirlos.
* Se crea un PIPELINE para estudiar los datos, limpiarlos, ordenarlos y analizarlos para obtener unas conclusiones.
* Finalmente se creará un modelo de Machine Learning.

## PIPELINE

![Pipeline image]()

* Se crea un notebook para visualizar datos y analizarlos en primer lugar.
* A partir de este notebook se crean los notebooks para acquisition, wrangling, analysis y reporting de datos.
* Acquisition:
* Wrangling: Se limpian los datos y se obtiene el dataset (Data) con el que se harán los analisis y reporting.
* Analysis:
* Reporting: Se muestran visualizaciones y se predice la insulina a administrar (MLmodel)

## Machine Learning Model (MLmodel)

* 1. Data Loading

* 2. EDA (Exploratory Data Analysis)

In Pipeline: acquisition, wrangling, analysis and reporting.

* 3. ML PREPROCESSING

* 4. Train a simple model


* 5. Check model performance on test and train data


* 6. Check model performance using cross validation

* 7. Optimize model using grid search


from sklearn.externals import joblib
joblib.dump(model, 'data/results/model.pkl')

## Technical requirements

* Para crear el repositorio se utiliza Conda, Bash y GitHub.

* Para la realización de Pipeline se utilizan: Conda, Bash, GitHub, Jupyter Notebooks, Python, Pandas, Numpy...

* Para la realización del modelo de Machine Learning



## Repositorio en GitHub



## Pipeline

Estructura de carpetas:


└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main.py
    ├── MLmodel.py
    ├── notebooks
    |   ├── acquisition.ipynb
    |   ├── analysis.ipynb
    │   ├── reporting.ipynb
    │   └── wrangling.ipynb
    ├── data
    |   ├── raw
    |   ├── processed
    |   └── results
    |
    ├── p_acquisition
    │   └── m_acquisition.py
    |
    ├── p_wrangling
    │   └── m_wrangling.py
    |
    ├── p_analysis
    |   └── m_analysis.py
    |
    └── p_reporting
        └── m_reporting.py
    


## Machine Learning Model






## Conclusions



## Author

Emilio José Patiño Rodrigo

