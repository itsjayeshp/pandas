'''
Simple Time Series Data Plotting




Importance★★★★☆
Difficulty★★☆☆☆
You are a data analyst at a retail company. Your manager has asked you to
analyze the sales data for the past 12 months and visualize it to identify any
trends or patterns.
Create a time series plot using Python to display the sales data.
Generate the sales data within your code.
The x-axis should represent the months, and the y-axis should represent the
sales figures.
Ensure that the plot is clear and well-labeled.

'''

# code 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
months = pd.date_range(start='2023-01-01', periods=12, freq='M')
sales = np.random.randint(1000, 5000, size=12)
data = pd.DataFrame({'Month': months, 'Sales': sales})
plt.figure(figsize=(10, 5))
plt.plot(data['Month'], data['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()