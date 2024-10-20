# Height vs Weight Scatter Plot


'''
Importance★★★★☆
Difficulty★★☆☆☆
A fitness center wants to analyze the relationship between the height and
weight of their clients to provide better personalized training programs.
You are tasked with creating a scatter plot to visualize this relationship.
Generate a sample dataset of 100 clients, each with random height (in cm)
and weight (in kg).
Use Python to create this scatter plot.

'''


# code

import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

np.random.seed(42)
height = [random.uniform(150, 200) for _ in range(100)]
weight = [random.uniform(50, 100) for _ in range(100)]
# print(height)

data = pd.DataFrame({'Height': height, 'Weight': weight})
plt.scatter(data['Height'], data['Weight'], alpha=0.6)
plt.title('Scatter Plot of Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
