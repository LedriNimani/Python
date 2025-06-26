import pandas as pd
import matplotlib.pyplot as plt

df=dp.read_csv("tokyo_data.csv")

filtered_DF=df[df["Average Temp"]>=15]

filtered_DF=filtered_DF.sort_values(by="Average Temp", ascending=False)

print(filtered_DF)
