import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

my_dataset=pd.read_csv("avgIQpercountry.csv")
my_datset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

fig=px.scatter_geo(my_dataset,locations="Country",locationmode="country names",
                   color="Continent",projection="natural earth",
                   hover_data=["Literacy Rate","Nobel Prices"],color_continuous_scale="agsunset",
                   title="Average IQ By Country")

fig.show()