# data project
# Martin Goff
import csv
import matplotlib.pyplot as plt

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # global variable
    station_list = []

    # all functions

    # iterates through data to get a full list of stations
    def make_station_list():
        global station_list
        for row in reader:
            station_list.append(row['STID'])
        # converts list of stations into dict then back into list to remove duplicates
        station_list = list(dict.fromkeys(station_list))
        return station_list

    # each function from here on out is in pairs: one creates a list of data, the other plots this data

    # makes a list of each maximum temp in a given month, next function plots it
    def max_temp(station, month):
        global reader
        max_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                max_list.append(float(row['TMAX']))
        csvfile.seek(0)
        return max_list

    # each of these plotting functions uses the station list to plot the data for each station, make a legend, give axis labels, and show the data
    def plot_max_temp(month):
        make_station_list()
        for station in station_list:
            plt.plot(max_temp(station, month))
            plt.legend(station_list)
        plt.xlabel('Days Into Month/2016')
        plt.ylabel('Maximum Temperatures (°F)')
        plt.show()

    # makes a list of each minimum temp in a given month, next function plots it
    def min_temp(station, month):
        global reader
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                min_list.append(float(row['TMIN']))
        csvfile.seek(0)
        return min_list

    def plot_min_temp(month):
        make_station_list()
        for station in station_list:
            plt.plot(min_temp(station, month))
            plt.legend(station_list)
        plt.xlabel('Days Into Month/2016')
        plt.ylabel('Minimum Temperatures (°F)')
        plt.show()

    # makes a list of each day's highest wind speed in a given month, next function plots it
    def highest_wind_speeds(station, month):
        global reader
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                min_list.append(float(row['WSMX']))
        csvfile.seek(0)
        return min_list

    def plot_wind_speeds(month):
        make_station_list()
        for station in station_list:
            plt.plot(highest_wind_speeds(station, month))
            plt.legend(station_list)
        plt.xlabel('Days Into Month/2016')
        plt.ylabel('Wind Speeds (mph)')
        plt.show()

    # makes a list of each day's average humidity in a given month, next function plots it
    def average_humidity(station, month):
        global reader
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                min_list.append(float(row['HAVG']))
        csvfile.seek(0)
        return min_list

    def plot_humidity(month):
        make_station_list()
        for station in station_list:
            plt.plot(average_humidity(station, month))
            plt.legend(station_list)
        plt.xlabel('Days Into Month/2016')
        plt.ylabel('Humidity (%)')
        plt.show()

    # makes a list of each day's rain totals in a given month, next function plots it
    def rain_totals(station, month):
        global reader
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station and row['MONTH'] == month:
                min_list.append(float(row['RAIN']))
        csvfile.seek(0)
        return min_list

    def plot_rain_totals(month):
        make_station_list()
        for station in station_list:
            plt.plot(rain_totals(station, month))
            plt.legend(station_list)
        plt.xlabel('Days Into Month/2016')
        plt.ylabel('Total Rainfall (in)')
        plt.show()


    # loop
    name = input("What is your name? ")
    while True:
        choice = input(f"\nWhat is the data you would like to see, {name}? \n"
        "Here are your choices: \n"
        "tmax: all the highs, \n"
        "tmin: all the lows, \n"
        "wsmx: the highest given wind speeds, \n"
        "havg: the average humidity, \n"
        "or rain: total precipitation in a day. ")

        # each choice asks for a month to plot (a whole year cannot be plotted with this code)
        # then each choice asks about quitting after the graph shown is closed
        if choice == 'tmax':
            month = input(f"\nWhich month would you like to see plotted, {name}? ")
            plot_max_temp(month)
            quit = input("\nDo you want to plot again? y or n: ")
            if quit == 'n':
                break
        elif choice == 'tmin':
            month = input(f"\nWhich month would you like to see plotted, {name}? ")
            plot_min_temp(month)
            quit = input("\nDo you want to plot again? y or n: ")
            if quit == 'n':
                break
        elif choice == 'wsmx':
            month = input(f"\nWhich month would you like to see plotted, {name}? ")
            plot_rain_totals(month)
            quit = input("\nDo you want to plot again? y or n: ")
            if quit == 'n':
                break
        elif choice == 'havg':
            month = input(f"\nWhich month would you like to see plotted, {name}? ")
            plot_humidity(month)
            quit = input("\nDo you want to plot again? y or n: ")
            if quit == 'n':
                break
        elif choice == 'rain':
            month = input(f"\nWhich month would you like to see plotted, {name}? ")
            plot_rain_totals(month)
            quit = input("\nDo you want to plot again? y or n: ")
            if quit == 'n':
                break
        # catch all for mistakes
        else:
            print("\nI don't recognize that choice.")