# Histogram Generation from Random Data


'''
Importance★★★★☆
Difficulty★★☆☆☆
You are a data analyst working for a marketing company.
The company wants to understand the distribution of customer ages in their
database.
Your task is to create a histogram that visualizes this distribution using
randomly generated age data.
Generate a dataset of 1000 customer ages, assuming the ages range from 18
to 80 years old.
Then, create a histogram to visualize the distribution of these ages.
Make sure to include appropriate labels and a title for the histogram.
The histogram should have 10 bins.
Use matplotlib for visualization.
Generate the sample data within your code.

'''


# code 


import numpy as np
import matplotlib.pyplot as plt

# Generate random age data
ages = np.random.randint(18,81,1000)

# Create the histogram
plt.figure(figsize=(10,6))
plt.hist(ages,bins=10,edgecolor='red')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Ages')

# Display the plot
# plt.show()