from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

import argparse



def argument_parser():
    my_parser = argparse.ArgumentParser(description = 'Set chart type or insline')
    my_parser.add_argument("-b", "--bar", help="Produce a barplot and line plot", action="store_true")
    my_parser.add_argument("-g", "--graph", help="Produce a graphic unique", action="store_true")
    my_parser.add_argument("-c", "--calc", help="Calculate insulin needed", action="store_true")
    args = my_parser.parse_args()
    if args.bar:
       print('\n Option: Barplot activate')
    if args.graph:
        print('\n Option: Unique graphic activate')
    if args.calc:
        print('\n Option: Insulin needed activate')
    return args

def main(args):
    if args.calc == True:
        food = int(input('Introduce las raciones a comer: '))
        mre.reference_data(food)
        mre.insuline_admin(args)
    elif args.bar == True:
        title_graphic = input('Enter the title: ')
        mac.acquire()
        Data = mwr.wrangle()
        by_hour_mean= mre.data_by_hour(Data)
        by_day_of_week_mean = mre.data_by_week(Data)
        mre.plotting_function(by_hour_mean,by_day_of_week_mean, title_graphic, args)
    elif args.graph == True:
        title_graphic = input('Enter the title: ')
        Data = mwr.wrangle()
        mre.plotting_graph(Data, title_graphic)

        print('______________Pipeline successfully completed_______________')



if __name__ == '__main__':
    args = argument_parser()
    main(args)







# Nota: Hay que escribir algo debajo de __main__ si no no funciona bien


