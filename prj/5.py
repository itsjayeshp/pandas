'''
Heatmap of Correlation Matrix



Importance★★★★☆
Difficulty★★★☆☆
You are a data analyst at a retail company, and you have been given a
dataset containing various sales metrics. Your task is to create a heatmap of
the correlation matrix to identify the relationships between different
metrics. This will help the company understand which metrics are closely
related and can influence each other.
Generate a sample dataset with at least five different sales metrics and
create a heatmap of the correlation matrix using Python. The heatmap
should clearly show the correlation values between the metrics.
Use the following code to generate the sample dataset:

'''


# code 


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(0)
data = pd.DataFrame({
'Sales': np.random.rand(100) * 1000,
'Profit': np.random.rand(100) * 500,
'Discount': np.random.rand(100) * 50,
'Customer_Age': np.random.randint(18, 70, size=100),
'Customer_Satisfaction': np.random.randint(1, 10, size=100)
})

correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.tight_layout()

plt.show()
