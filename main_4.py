import pandas as pd

# Pandas - Data Correlations
print("\n Pandas - Data Correlations\n===============================")

# Finding Relationships
# A great aspect of the Pandas module is the corr() method.
# The corr() method calculates the relationship between each column in your data set.
# The examples in this page uses a CSV file called: 'data.csv'.
# Download data.csv. or Open data.csv
df = pd.read_csv('data_4.csv')

print("\n Finding Relationships\n===============================")
# df.corr() Show the relationship between the columns:
print(df.corr())

print("\n Pandas - Plotting\n===============================")
# Plotting
# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
# Read more about Matplotlib in our Matplotlib Tutorial.
import matplotlib.pyplot as plt
df = pd.read_csv('data_4.csv')
# df.plot()
# plt.show()

print("\n Scatter Plot\n===============================")
# Specify that you want a scatter plot with the kind argument:
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis.
# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
# Include the x and y arguments like this:
# x = 'Duration', y = 'Calories'
# Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we concluded with the fact that higher duration means more calories burned.
df = pd.read_csv('data_4.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

# A scatterplot where there are no relationship between the columns:
df = pd.read_csv('data_4.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# plt.show()

print("\n Histogram\n===============================")
# Use the kind argument to specify that you want a histogram:
# kind = 'hist'
# A histogram needs only one column.
# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
# In the example below we will use the "Duration" column to create the histogram:
df["Duration"].plot(kind = 'hist')
plt.show()

# print("\n ______\n===============================")