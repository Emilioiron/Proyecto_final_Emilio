from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

import argparse

def main():
    argument_parser()

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Set chart type or insline')
    parser.add_argument("-b", "--bar", help="Produce a barplot", action="store_true")
    parser.add_argument("-g", "--graph", help="Produce a graphic unique", action="store_true")
    parser.add_argument("-c", "--calc", help="Calculate insulin needed", action="store_true")
    args = parser.parse_args()
    return args
    #if args.bar:
    #    print('Option barplot and lineplot are activates')
    #if args.graph:
    #    print('Option unique graphic activate')
    #if args.calc:
    #    print('Option insulin needed activate')
    #return args

    #food = int(input('Introduce las raciones a comer: '))

    mre.reference_data(food)
    #arguments = argument_parser()
    mre.insuline_admin(args)


    #title_graphic = input('Enter the title: ')
    mac.acquire()
    Data = mwr.wrangle()
    by_hour_mean= mre.data_by_hour(Data)
    by_day_of_week_mean = mre.data_by_week(Data)
    mre.plotting_function(by_hour_mean,by_day_of_week_mean, title_graphic, args)
    print('______________Pipeline successfully completed_______________')





if __name__ == '__main__':
    main()
    food = int(input('Introduce las raciones a comer: '))
    title_graphic = input('Enter the title: ')

    #main(arguments)






# Nota: Hay que escribir algo debajo de __main__ si no no funciona bien


