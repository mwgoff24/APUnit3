# data lab 2
import csv

with open('BigData2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    def define_max_and_min(station):
        global reader
        max_list = []
        min_list = []
        for row in reader:
            if row['TMAX'] != "-996.00" and row[station]:
                max_list.append(float(row['TMAX']))
        print(max_list)