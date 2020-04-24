import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def acquire():

    df1 = pd.read_csv('./data/raw/data_1.csv')
    df2 = pd.read_csv('./data/raw/data_2.csv')
    list_df = [df2, df1]
    data_all_parameters = pd.concat(list_df, ignore_index=False, axis=0, sort=False)
    data_all_parameters.to_csv('./data/raw/data_all_parameters.csv')

    return data_all_parameters


