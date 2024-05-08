import pandas as pd

print("\n Pandas - Cleaning Empty Cells\nRemove Rows\n===============================")
df = pd.read_csv('data_2.csv')

new_df = df.dropna() # Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

print(new_df.to_string())

# If you want to change the original DataFrame, use the inplace = True argument:
df.dropna(inplace = True)
print(df.to_string())

print("\n Replace Empty Values\n===============================")
df = pd.read_csv('data_2.csv')
df.fillna(130, inplace = True)
print(df.to_string())

print("\n Replace Only For Specified Columns\n===============================")
# Replace NULL values in the "Calories" columns with the number 130:
df = pd.read_csv('data_2.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())

print("\n Replace Using Mean, Median, or Mode\n===============================")
# Calculate the MEAN, and replace any empty values with it:
df = pd.read_csv('data_2.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string()) # As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68

# Calculate the MEDIAN, and replace any empty values with it:
df = pd.read_csv('data_2.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string()) # As you can see in row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2

# Calculate the MODE, and replace any empty values with it:
df = pd.read_csv('data_2.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string()) # As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0
