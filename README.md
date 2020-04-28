
![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)



# Machine learning model to predict a diabetic's insulin injection

Final Ironhack Project

## Description

### Objective

* The aim of this project is to create a Machine Learning model that predicts the insulin that a type I diabetic has to inject from the data obtained from the person's insulin pump.

* Different studies have been carried out in Spain and around the world which conclude that diabetes is a disease that is affecting an increasing percentage of the population, year after year the number of people with type 1 and type 2 diabetes is increasing. This project would be an initial phase to be able to help especially type 1 diabetics to improve their quality of life and not to have serious diseases in the future related to diabetes.

* Here I leave link data of [Spain](https://www.ciberdem.org/noticias/ciberdem-publica-los-resultados-del-estudio-di-betes-sobre-la-incidencia-de-la-enfermedad-en-espana) and at [world](https://www.who.int/diabetes/es/)

### Needs of a diabetic

* Depending on the carbohydrates a person eats, the pancreas delivers more or less insulin immediately. Type 1 diabetics do not have a working pancreas and need to inject insulin every time they eat. 

* It is difficult to adjust the insulin to what a diabetic eats at any given time and this is a problem many times for them as they can have very high or very low blood glucose levels due to miscalculation and this can lead to serious health problems or even death, in the long run.

* This model calculates the units of insulin that a diabetic needs according to what they eat from the parameters that their insulin pump has (personalized), time and day of the week.


## Steps I have followed

* A repository is created for the project with the name "Emilio_End_Project".
* Download the insulin pump (Medtronic) data from your Carelink application
* Data is downloaded from June 2015 to March 2020.
* The data cannot be downloaded in a personalized way with a start and end date for more than three months, so you have to download 20 files in CSV format to join them later.
* A PIPELINE is created to study the data, clean it, order it and analyze it to obtain some conclusions.
* Finally a model of Machine Learning will be created.


## PIPELINE

![Pipeline image](pipelines.jpg)

* A notebook is created to display data and analyze it first.
* From this notebook, notebooks are created for data acquisition, wrangling, analysis and reporting.
* Acquisition:
* Wrangling: The data is cleaned and the dataset is obtained, with which the analysis and reporting will be done.
* Analysis:
* Reporting: Visualizations are shown and the insulin to be administered is predicted (MLmodel)


## Machine Learning Model (MLmodel)

* 1. Data Loading

* 2. EDA (Exploratory Data Analysis)

In Pipeline: acquisition, wrangling, analysis and reporting.

* 3. ML PREPROCESSING

* Train a simple model

* 5. Check model performance on test and train data

* 6. Check model performance using cross validation

* Optimize model using grid search 



## Technical requirements

* Conda, Bash and GitHub are used to create the repository.

* To create the Pipeline we use: Conda, Bash, GitHub, Jupyter Notebooks, Python, Pandas, Numpy...

* For the realization of the Machine Learning model: Sklearn and its libraries, Pipeline, StandarScaler, OneHotEncoder, Train-test-split, mean_squared_error, r2_score.

* To connect the trained model to the final calculation and to be able to make the prediction you use joblib...



## Estructura de carpetas:

```
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
 
 ```

## Conclusions

The model simulates the insulin to be injected for a diabetic according to the parameters of his insulin pump with minimal error.

## Enhancements

* Calculate the carbohydrate rations according to the food or meal
* Do web scraping to get the carbohydrates from food and meals.
* Connect the application to a smartwatch to make it more real and accurate.
* Make a personalized mobile app for each diabetic.


## Acknowledgment

I appreciate the help provided by the Leads and Assistant Teachers, always answering questions and providing solutions.

I thank and dedicate the project to my wife, Estefi, since without her I would not have been able to carry out it, on the one hand, because of the information provided and, on the other hand, for allowing me to have the necessary dedication to finish it.

## Author

Emilio José Patiño Rodrigo


![APM](https://img.shields.io/apm/l/rretreterte)