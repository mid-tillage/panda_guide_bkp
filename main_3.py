import pandas as pd

print("\n Pandas - Cleaning Data of Wrong Format\nRemove Rows\n===============================")
# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

print("\n Convert Into a Correct Format\n===============================")
import pandas as pd
df = pd.read_csv('data_3.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# Convert Into a Correct Format
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

print("\n Removing Rows\n===============================")
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

print("\n Pandas - Fixing Wrong Data\n===============================")
print("\n Wrong Data\n===============================")
# "Wrong data" does not have to be "empty cells" or "wrong format", it can sust be wrong, like if someone registered "199" instead of "1.99".
# Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
# If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
# It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

print("\n Replacing Values\n===============================")
df.loc[7, 'Duration'] = 45
print(df.to_string())

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.
df = pd.read_csv('data_3.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())

print("\n Removing Rows\n===============================")
# Delete rows where "Duration" is higher than 120:
df = pd.read_csv('data_3.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())

print("\n Pandas - Removing Duplicates\n===============================")
print("\n Discovering Duplicates\n===============================")
# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

print("\n Removing Duplicates\n===============================")
df.drop_duplicates(inplace = True)
print(df.to_string())

# ************************
#  Insert the correct syntax for replacing empty cells with the value "130".
df.fillna(130)
