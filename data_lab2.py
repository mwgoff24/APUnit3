# data lab 2
import csv

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # function to iterate through data and find max and min of each station
    def define_max_and_min(station):
        global reader
        max_list = []
        min_list = []
        for row in reader:
            # basically same concept as the previous lab but now the code applies only to a specific station
            if row['TMAX'] != "-996.00" and row['STID'] == station:
                max_list.append(float(row['TMAX']))
            if row['TMIN'] != "-996.00" and row['STID'] == station:
                min_list.append(float(row['TMIN']))
        print(f"{station} high: {max(max_list)}")
        print(f"{station} low: {min(min_list)}")
        # resets iteration to top of data so function can run again
        csvfile.seek(0)

    define_max_and_min('ARD2')

    define_max_and_min('BEAV')

    define_max_and_min('BOIS')

    define_max_and_min('CENT')

    define_max_and_min('NRMN')

    define_max_and_min('STIL')

    define_max_and_min('TISH')

    define_max_and_min('TULN')
    
    define_max_and_min('WOOD')