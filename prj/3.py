# Plotting a Sine Wave with Matplotlib

'''
Importance★★★★☆
Difficulty★★☆☆☆
A local weather station wants to visualize temperature fluctuations
throughout the day.
They've asked you to create a sine wave plot that represents the typical
daily temperature pattern.
Your task is to generate a sine wave using numpy, and then plot it using
matplotlib.
The x-axis should represent 24 hours of the day, and the y-axis should
represent temperature in Celsius.
The sine wave should have an amplitude of 5°C and be centered around
20°C.
Please create the input data within your code and produce a clear, labeled
plot.
Make sure to include appropriate titles and labels for the axes



'''


# code

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,24,100)
# print(x)

y = 5 * np.sin(2 * np.pi * x / 24) + 20

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Daily Temperature Fluctuation')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(np.arange(0, 25, 4))
plt.ylim(10, 30)

plt.show()