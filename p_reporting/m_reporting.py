import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from IPython.display import set_matplotlib_formats
from sklearn.externals import joblib
import datetime
from datetime import date

set_matplotlib_formats('svg')
sns.set_style('whitegrid')

def reference_data(food):
    new_food_dict = {'Unnamed: 0': {0: 0},
                     'Unnamed: 0.1': {0: 16},
                     'Basal Rate (U/h)': {0: 2.2},
                     'BWZ Estimate (U)': {0: 9.5},
                     'BWZ Carb Ratio (U/Ex)': {0: 1.5},
                     'BWZ Insulin Sensitivity (mg/dL/U)': {0: 50.0},
                     'BWZ Carb Input (exchanges)': {0: 9.5},
                     'BWZ BG Input (mg/dL)': {0: 84.0},
                     'BWZ Correction Estimate (U)': {0: 0.2},
                     'BWZ Food Estimate (U)': {0: 5},
                     'BWZ Active Insulin (U)': {0: 0.1},
                     'BWZ Unabsorbed Insulin Total (U)': {0: 0.5},
                     'day_of_month': {0: 25},
                     'day_of_week': {0: 2},
                     'month_of_year': {0: 3},
                     'hour': {0: 10}}

    # Actualización de datos, fecha y comida a tomar:
    new_food_dict['day_of_month'][0] = date.today().day
    new_food_dict['month_of_year'][0] = date.today().month
    new_food_dict['hour'][0] = datetime.datetime.now().hour
    new_food_dict['day_of_week'][0] = datetime.datetime.today().weekday()
    new_food_dict['BWZ Carb Input (exchanges)'][0] = food
    new_food_dict['BWZ Food Estimate (U)'][0] = food
    new_food_today = pd.DataFrame(new_food_dict).to_csv('./data/results/new_food_today.csv')
    return



def insuline_admin(args):

    new_food_today = pd.read_csv('./data/results/new_food_today.csv')
    model_pickle = joblib.load('./data/results/model.pkl')
    administrar_insulina = model_pickle.predict(new_food_today)
    print(f'Te debes administrar '
            + pd.DataFrame(administrar_insulina).iloc[0, 0].round(2).astype(str)
            + ' unidades de insulina')

def data_by_hour(df):
    df['hour'] = df['hour'].astype(int)
    by_hour = df.sort_values('hour')
    by_hour_mean = by_hour.groupby(['hour']).mean()
    return by_hour_mean

def data_by_week(df):
    by_day_of_week = df.sort_values('hour')
    by_day_of_week_mean = by_day_of_week.groupby(['day_of_week']).sum()
    return   by_day_of_week_mean

def plotting_function(df_hour,df_day, title, args):

    fig, ax = plt.subplots(2, 2,figsize=(4, 4), constrained_layout=True)
    plt.suptitle(title, fontsize=25)
    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (1, 0))
    ax3 = plt.subplot2grid((2, 2), (0, 1))
    ax4 = plt.subplot2grid((2, 2), (1, 1))

    x = df_hour.index.astype(str).tolist()

    #plt.subplot(221)
    #plt.grid(True)
    ax1.bar(x, df_hour['BWZ Carb Input (exchanges)'], color = 'blue')
    #ax1.set_xticklabels(ax2.get_xticklabels(all))
    ax1.set_xlabel('Hour')
    ax1.set_ylabel('Carb Input.U insulin')
    #ax1.set_title(title, fontsize=20)
    plt.tight_layout()
    #plt.colorbar(pos, ax=ax1)

    #plt.subplot(222)
    #plt.grid(True)
    ax2.bar(x, df_hour['BWZ Estimate (U)'], color = 'olive' )
    #ax2.set_xticklabels(ax2.get_xticklabels               ())
    ax2.set_xlabel('Hour')
    ax2.set_ylabel('BWZ Estimate (U)')
    #ax2.set_title(title, fontsize=16)
    plt.tight_layout()

    #plt.subplot(223)
    #plt.grid(True)
    day_of_week = ['L','M','X', 'J','V','S','D']
    ax3.plot( day_of_week, 'BWZ Carb Input (exchanges)',
            data=df_day, marker='o', markerfacecolor='blue',
            markersize=8, color='skyblue', linewidth=2)
    ax3.set_xlabel('Day of week')
    ax3.set_ylabel('BWZ Carb Input')
    plt.tight_layout()

    #plt.subplot(224)
    #plt.grid(True)
    ax4.plot( day_of_week, 'BWZ Estimate (U)',
            data=df_day, marker='o', color='olive', linewidth=2)
    ax4.set_xlabel('Day of week')
    ax4.set_ylabel('BWZ Estimate')
    plt.tight_layout()

    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
    plt.show()
    fig.savefig('./data/results/' + title + '.pdf', format='pdf')





def plotting_graph(df, title):
    df['hour'] = df['hour'].astype(int)
    by_hour = df.sort_values('hour')
    sns.set(style="whitegrid")  # Estilo trazado

    fig = plt.figure(figsize=(8, 4))
    sns.barplot(x='hour', y='BWZ Carb Input (exchanges)', data=by_hour)
    plt.show()
    fig.savefig('./data/results/graph' + title + '.pdf', format='pdf')

