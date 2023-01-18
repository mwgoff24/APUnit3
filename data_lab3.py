import csv
import matplotlib.pyplot as plt

import numpy as np

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # station_list = []
    # for row in reader:
    #     station_list.append(row['STID'])
    # station_list = list(dict.fromkeys(station_list))
    # print(station_list)

    def define_max(station):
        global reader
        max_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station:
                max_list.append(float(row['TMAX']))
        csvfile.seek(0)
        return max_list

    plt.plot(define_max('ARD2'))
    plt.plot(define_max('BEAV'))
    plt.plot(define_max('BOIS'))
    plt.plot(define_max('CENT'))
    plt.plot(define_max('NRMN'))
    plt.plot(define_max('STIL'))
    plt.plot(define_max('TISH'))
    plt.plot(define_max('TULN'))
    plt.plot(define_max('WOOD'))
    plt.xlabel('days into year')
    plt.ylabel('max temps (°F)')
    plt.show()