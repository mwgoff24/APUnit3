import csv
import matplotlib.pyplot as plt

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    station_list = []

# adds each station to the empty station list above
    def make_station_list():
        global station_list
        for row in reader:
            station_list.append(row['STID'])
        # converts list of stations into dict then back into list to remove duplicates
        station_list = list(dict.fromkeys(station_list))
        return station_list

# creates a max list for each station but not a min list
    def define_max(station):
        global reader
        max_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station:
                max_list.append(float(row['TMAX']))
        # moves counter back to top of csv file
        csvfile.seek(0)
        # needs to return list to display a graph of data
        return max_list

# plots all data by making station list and plotting the graph for each station in said list
    def plot_data():
        make_station_list()
        for station in station_list:
            plt.plot(define_max(station))
            plt.legend(station_list)

# defines x and y labels, plots all points, then displays graph
    plt.xlabel('Days Into 2016')
    plt.ylabel('Maximum Temperatures (°F)')
    plot_data()
    plt.show()