import pandas as pd

data = pd.read_csv(r"E:\dataset\test.csv", encoding="latin-1")
print(data.head(5))
print(data.info())
print(data.describe())