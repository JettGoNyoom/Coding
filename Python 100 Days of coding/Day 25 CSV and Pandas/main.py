# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])