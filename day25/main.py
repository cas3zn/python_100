# reading weather_data.csv line by line using python

# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temp_value = int(row[1])
#             temperatures.append(temp_value)
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
