import pandas as pd

mydict = {
    "day1":450,
    "day2":800,
    "day3":900
}

df = pd.DataSeries(mydict)
print(df)