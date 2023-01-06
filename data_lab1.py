# data lab
import csv

# data of maximum temperatures
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # finding the max value

    # first a list is made to store float values of max temps
    max_temp_list = []
    for row in reader:
        # conditional checks for "bad" temps and passes them
        if row['TMAX'] != "-996.00":
            # if temp is not bad recording, temp is appended to list
            max_temp_list.append(float(row['TMAX']))

    max_average = sum(max_temp_list) / len(max_temp_list)

    # prints the highest max and average max
    print(f"Highest maximum temperature: {max(max_temp_list)} °F")
    # avg prints a rounded value for aesthetic reasons
    print(f"Average maximum all year: {round(max_average, 2)} °F \n")

# same coding as above but with minimum values
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # finding the min value 

    min_temp_list = []
    for row in reader:
        if row['TMIN'] != "-996.00":
            min_temp_list.append(float(row['TMIN']))

    min_average = sum(min_temp_list) / len(min_temp_list)
    print(f"Lowest minimum temperature: {min(min_temp_list)} °F")
    print(f"Average minimum all year: {round(min_average, 2)} °F")