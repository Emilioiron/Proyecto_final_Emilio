
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre


food = int(input('Introduce las raciones a comer: '))
mre.reference_data(food)
mre.insuline_admin()

title_graphic = input('Enter the title: ')
mac.acquire()
Data = mwr.wrangle()
by_hour_mean= mre.data_by_hour(Data)
by_day_of_week_mean = mre.data_by_week(Data)
mre.plotting_function(by_hour_mean,by_day_of_week_mean, title_graphic)



if __name__ == '__main__':
    print('Pipeline successfully completed')





# Nota: Hay que escribir algo debajo de __main__ si no no funciona bien


