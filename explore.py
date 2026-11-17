# Self-Assessment 1:
# A boolean filter keeps only the rows that match a condition.
# For example, it can show only sales from the South region.

# Self-Assessment 2:
# df["revenue"] returns a Series, which is one dimensional.
# df[["revenue"]] returns a DataFrame, which is two dimensional.
# This matters when a function needs a specific data structure.

# Self-Assessment 3:
# I would choose pandas because it can analyze large amounts of data
# in a very short time. It also makes the work easier because I can
# run the same code again without doing everything manually.

import pandas as pd

# Exercise 1:
df = pd.read_csv("data/retail_sales.csv")

print("First 5 rows:")
print(df.head())

print("Shape:")
print(df.shape)

print("Columns:")
print(df.columns.tolist())

print("Data types:")
print(df.dtypes)

# Exercise 2:
south = df[df["region"] == "South"]

print("Number of South orders:")
print(len(south))

print("First 5 South orders:")
print(south.head())

# Exercise 3:
top5 = df.sort_values("revenue", ascending=False).head(5)

print("Top 5 orders by revenue:")
print(top5)

# Exercise 4:
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("Number of big South orders:")
print(len(big_south))

print("First 5 big South orders:")
print(big_south.head())

# Exercise 5:
df["per_unit"] = df["revenue"] / df["quantity"]

print("First 5 rows with per_unit:")
print(df.head())

print("Average revenue per unit:")
print(df["per_unit"].mean())

# Exercise 6:
print("Unique regions:")
print(df["region"].unique())

print("Number of orders by region:")
print(df["region"].value_counts())

# Exercise 7:
selected_df = df[["region", "product", "revenue"]]

print("Selected columns:")
print(selected_df.head())

print("Shape of selected DataFrame:")
print(selected_df.shape)

# Exercise 8:
df.to_csv("data/explored.csv", index=False)

print("Data saved to explored.csv")