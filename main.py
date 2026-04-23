import pandas as pd

df = pd.read_csv("sales.csv")   # looks for sales.csv in the same folder as main.py
print(df.head())

print(df.shape)        # rows and columns
print(df.info())       # column types
print(df.describe())   # summary statistics

df = df.dropna()       # remove missing values
df["Revenue"] = df["Revenue"].astype(int)  # ensure numeric type

print("Average revenue:", df["Revenue"].mean())
print("Revenue by region:\n", df.groupby("Region")["Revenue"].mean())

import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart
df.groupby("Region")["Revenue"].mean().plot(kind="bar")
plt.show()

# Histogram
sns.histplot(df["Revenue"], bins=5)
plt.show()


