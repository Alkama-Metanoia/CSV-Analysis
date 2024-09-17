###  1st way
# with open("weather_data.csv") as data_file:
#      data = data_file.readlines()
#     print(data)

### 2nd way to do it

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data
# #print(data.temp.max())
# print(data[data.temp == data.temp.max()])

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel)
print(Cinnamon_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, Cinnamon_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
