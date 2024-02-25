import pandas
import random
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 22,
    "Sunday": 24
}

weather_f = {name: (value * 9/5) + 32 for(name, value) in weather_c.items()}
print(weather_f)
