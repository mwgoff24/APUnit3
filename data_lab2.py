# data lab 2
import csv

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    def define_max_and_min(station):
        global reader
        max_list = []
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row['STID'] == station:
                max_list.append(float(row['TMAX']))
            if row['TMIN'] != "-996.00" and row['STID'] == station:
                min_list.append(float(row['TMAX']))
        print(max_list)
        print(min_list)
        # print(f"{station} high: {max(max_list)}")
        # print(f"{station} low: {min(min_list)}")

    define_max_and_min('ARD2')

    define_max_and_min('BEAV')

    define_max_and_min('BOIS')

    define_max_and_min('CENT')

    define_max_and_min('NRMN')

    define_max_and_min('STIL')

    define_max_and_min('TISH')

    define_max_and_min('TULN')
    
    define_max_and_min('WOOD')