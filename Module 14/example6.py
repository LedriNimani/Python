import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

my_dataset=pd.read_csv("avgIQpercountry.csv")

my_dataset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

numeric_iq_data_loc=my_dataset.select_dtypes(include=['number'])

sns.heatmap(numeric_iq_data_loc.corr(),annot=True)

#pip install seaborn
#pip install plotly