import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from IPython.display import set_matplotlib_formats

set_matplotlib_formats('svg')
sns.set_style('whitegrid')

Data = pd.read_csv('./data/processed/Data.csv')

def data_by_hour(df):
    df['hour'] = df['hour'].astype(int)
    by_hour = df.sort_values('hour')
    by_hour_mean = by_hour.groupby(['hour']).mean()
    return by_hour_mean

def data_by_week(df):
    by_day_of_week = Data.sort_values('hour')
    by_day_of_week_mean = by_day_of_week.groupby(['day_of_week']).sum()
    return   by_day_of_week_mean

def plotting_function(df_hour,df_day, title):

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

    return 


#def save_viz(fig, title):
#    fig.savefig('./data/results/' + title + '.pdf', format='pdf')
