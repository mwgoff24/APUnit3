import csv

with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if row['TMIN'] == "-996.00":
            print(f"Day: {row['MONTH']}/{row['DAY']}")