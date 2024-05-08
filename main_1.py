import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(pd.__version__)
print(myvar)

a = [1, 7, 2]

myvar2 = pd.Series(a)

print(myvar2[0])

# Create Labels
print("Create labels\n===============================")
b = [1, 7, 2]
myvarb = pd.Series(b, index = ["first", "second", "third"])

print(myvarb)
print("third value: " + str(myvarb["third"]))

# Key/Value Objects as Series
print("Key/Value Objects as Series\n===============================")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
## To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# DataFrames
print("\nDataFrames\n===============================")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(myvar)

# Locate Row
print("\nLocate Row\n===============================")
#refer to the row index:
print(df.loc[0])
# Return row 0 and 1:
#use a list of indexes:
print(df.loc[[0, 1]]) # Note: When using [], the result is a Pandas DataFrame.

# Named Indexes
print("\nNamed Indexes\n===============================")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

print("\nLocate Named Indexes\n===============================")
#refer to the named index:
print(df.loc["day2"])

print("\nLoad Files Into a DataFrame\n===============================")
df = pd.read_csv('data_1.csv')
print(df) 

print("\n Read CSV Files\n===============================")
df = pd.read_csv('data_1.csv')
print(df.to_string()) # use to_string() to print the entire DataFrame.

print("\n max_rows\n===============================") # Check the number of maximum returned rows:
print("max rows: " + str(pd.options.display.max_rows))

pd.options.display.max_rows = 160
df = pd.read_csv('data_1.csv')
print(df) 
pd.options.display.max_rows = 60
print("max rows: " + str(pd.options.display.max_rows)) 

print("\n Read JSON\n===============================")
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world 
# of programming, including Pandas.
# In our examples we will be using a JSON file called 'data.json'.
df = pd.read_json('data.json')

print(df.to_string())
# Tip: use to_string() to print the entire DataFrame.

print("\n Dictionary as JSON\n===============================") # If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

print("\n Viewing the Data\n===============================")
df = pd.read_csv('data_1.csv')
print(df.head(9))

df = pd.read_csv('data_1.csv') # Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())

print(df.tail()) # Print the last 5 rows of the DataFrame:

print("\n Info About the Data\n===============================")
print(df.info()) 
# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.

print("\n Data Cleaning\n===============================")
# Data cleaning means fixing bad data in your data set.
# Bad data could be:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

print("\n Our Data Set\n===============================")
