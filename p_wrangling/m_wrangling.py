
import pandas as pd

def wrangle():
    df = pd.read_csv('./data/raw/data_all_parameters.csv')

# Se definen drop_columns y se borran.
    drop_columns = ['New Device Time', 'BG Reading (mg/dL)',\
                    'Linked BG Meter ID', 'Temp Basal Amount',\
                    'Temp Basal Type', 'Temp Basal Duration (h:mm:ss)', 'Bolus Type',\
                    'Bolus Volume Selected (U)', 'Bolus Volume Delivered (U)',\
                    'Bolus Duration (h:mm:ss)', 'Prime Type', 'Prime Volume Delivered (U)',\
                    'Alarm', 'Suspend', 'Rewind', \
                   'BWZ Target High BG (mg/dL)', 'BWZ Target Low BG (mg/dL)',\
                   'Sensor Calibration BG (mg/dL)',\
                   'Sensor Glucose (mg/dL)', 'ISIG Value', 'Event Marker', 'Bolus Number',\
                   'Bolus Cancellation Reason',\
                   'Final Bolus Estimate', 'Scroll Step Size', 'Insulin Action Curve Time',\
                   'Sensor Calibration Rejected Reason', 'Preset Bolus', 'Bolus Source',\
                   'Network Device Associated Reason',\
                   'Network Device Disassociated Reason',\
                   'Network Device Disconnected Reason', 'Sensor Exception',\
                   'Preset Temp Basal Name']
    data_cols_goods = df.drop(drop_columns, axis=1)

    # Rellenamos los valores nulos de las columnas según los valores que hay por encima.
    # Por el orden en el que salen en el archivo csv necesitamos hacer foward fill (ffill) a BWZ Unabsorbed
    # insulin Total(U/h)
    # y necesitamos hacer back fill (bfill) a la columna de Basal Rate (U/h)


    data_cols_goods['Basal Rate (U/h)'] = data_cols_goods['Basal Rate (U/h)'].fillna(method ='bfill')
    data_cols_goods['BWZ Unabsorbed Insulin Total (U)']= \
                  data_cols_goods['BWZ Unabsorbed Insulin Total (U)'].fillna(method ='ffill')


    # Se eliminan las filas con nulos
    data_without_nulls = data_cols_goods.dropna()
    # Para poder utilizar los valores de la columna Date y Time después hay que pasarlos a formato 'datetime'
    data_without_nulls['Date'] = pd.to_datetime(data_without_nulls['Date'])
    data_without_nulls['Time'] = pd.to_datetime(data_without_nulls['Time'])

    # Obtenemos features de las columnas 'Date' y 'Time'
    data_without_nulls['day_of_month'] = data_without_nulls['Date'].dt.day
    data_without_nulls['day_of_week'] = data_without_nulls['Date'].dt.dayofweek
    data_without_nulls['month_of_year'] = data_without_nulls['Date'].dt.month
    data_without_nulls['hour'] = data_without_nulls['Time'].dt.hour

    # Se eliminan las filas duplicadas
    data_without_duplicates = data_without_nulls.drop_duplicates()

    # Se eliminan las columnas 'Date' y 'Time' ya que se han formado las columnas
    # 'day_of_month', 'day_of_week', 'month_of_year' y 'hour' (datos categóricos) a partir de ellas.

    data_without_Date_and_Time = data_without_nulls.drop(['Date', 'Time'], axis=1)

    # Filtro
    filter_low_index = data_without_Date_and_Time['BWZ BG Input (mg/dL)'] < 70
    filter_high_index = data_without_Date_and_Time['BWZ BG Input (mg/dL)'] > 140

    # Eliminamos datos que no son buenos para realizar el entrenamiento, es decir, datos de lectura
    # de niveles de insulina altos o bajos aplicando un filtro.
    a = data_without_Date_and_Time[~(filter_low_index | filter_high_index)]

    Data = a.reset_index(drop=True)  # Drop = True para que no aparezca el index antiguo

    # Se pasa a categórica las columnas ['day_of_month', 'day_of_week', 'month_of_year', 'hour']
    Data['day_of_month'] = Data['day_of_month'].astype(str)
    Data['day_of_week'] = Data['day_of_week'].astype(str)
    Data['month_of_year'] = Data['month_of_year'].astype(str)
    Data['hour'] = Data['hour'].astype(str)

    Data.to_csv('./data/processed/Data.csv')

    return Data

