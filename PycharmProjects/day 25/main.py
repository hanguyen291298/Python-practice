import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
dic_color = {}
total_black = data[data["Primary Fur Color"] == "Black"].count()["Primary Fur Color"]
total_gray = data[data["Primary Fur Color"] == "Gray"].count()["Primary Fur Color"]
total_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"].count()["Primary Fur Color"]

dic_color["Black"] = total_black
dic_color["Gray"] = total_gray
dic_color["Cinnamon"] = total_cinnamon

new_data = pandas.DataFrame(dic_color)
print(new_data)



