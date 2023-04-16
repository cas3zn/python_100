# # reading weather_data.csv line by line using python
#
# with open("weather_data.csv") as weather:
#     data_csv = weather.readlines()
#     # print(data_csv)
#
# import csv
# with open("weather_data.csv") as weather:
#     weather_data = csv.reader(weather)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temp_value = int(row[1])
#             temperatures.append(temp_value)
#     # print(temperatures)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 9/5 + 32)
#
# # Create a dataframe from scratch
# import pandas
#
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_file.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

squirrels = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(squirrels)
df.to_csv("squirrel_count.csv")
