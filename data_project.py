# data project
# Martin Goff
import csv
import matplotlib.pyplot as plt

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    station_list = []

    # all functions

    def make_station_list():
        global station_list
        for row in reader:
            station_list.append(row['STID'])
        # converts list of stations into dict then back into list to remove duplicates
        station_list = list(dict.fromkeys(station_list))
        return station_list

    def max_temp(station, month):
        global reader
        max_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and month == '0':
                max_list.append(float(row['TMAX']))
            elif row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                max_list.append(float(row['TMAX']))
        csvfile.seek(0)
        return max_list

    def plot_max_temp(month):
        make_station_list()
        for station in station_list:
            plt.plot(max_temp(station, month))
            plt.legend(station_list)
        plt.show()

    def min_temp(station, month):
        global reader
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and month == '0':
                min_list.append(float(row['TMIN']))
            elif row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                min_list.append(float(row['TMIN']))
        csvfile.seek(0)
        return min_list

    def plot_min_temp(month):
        make_station_list()
        for station in station_list:
            plt.plot(min_temp(station, month))
            plt.legend(station_list)
        plt.show()

    def highest_wind_speeds(station, month):
        pass

    def average_humidity(station, month):
        pass

    def rain_totals(station, month):
        pass

    # loop
    name = input("What is your name? ")
    while True:
        choice = input("What is the data you would like to see? \n"
        "Here are your choices: \n"
        "tmax: all the highs, \n"
        "tmin: all the lows, \n"
        "wsmx: the highest given wind speeds, \n"
        "havg: the average humidity, \n"
        "or rain: total precipitation in a day. ")
        if choice == 'tmax':
            month = input("Which month would you like to see plotted? Type 0 for the whole year. ")
            if month == '0':
                plot_max_temp(month)
            else:
                plot_max_temp(month)
        elif choice == 'tmin':
            month = input("Which month would you like to see plotted? Type 0 for the whole year. ")
            if month == '0':
                plot_min_temp(month)
            else:
                plot_min_temp(month)
        elif choice == 'wsmx':
            pass
        elif choice == 'havg':
            pass
        elif choice == 'rain':
            pass
        else:
            print("\nI don't recognize that choice. \n")