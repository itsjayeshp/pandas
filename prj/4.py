# Creating Box Plots of Exam Scores

'''
Importance★★★★☆
Difficulty★★★☆☆
You are a data analyst working for a school district.
The principal has asked you to analyze the exam scores of students from
different classes to compare their performance.
Your task is to create a box plot that visualizes the distribution of exam
scores for each class.
The data consists of exam scores for three classes: Class A, Class B, and
Class C.
Each class has 30 students.
The scores are on a scale of 0 to 100.
Your objectives are:
Generate sample data for the three classes.
Create a box plot using matplotlib to compare the exam scores across the
three classes.
Properly label the x-axis with class names and the y-axis with "Exam
Scores".
Add a title to the plot: "Comparison of Exam Scores Across Classes".
Display the plot.
Write a Python script that accomplishes these tasks.
Make sure to use appropriate data structures and matplotlib functions to
create an informative and visually appealing box plot.

'''

# code


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
# Generate sample data for three classes
class_a = np.random.normal(75, 10, 30).clip(0, 100)
class_b = np.random.normal(70, 15, 30).clip(0, 100)
class_c = np.random.normal(80, 8, 30).clip(0, 100)

# print(class_a)


# Combine data into a list
data = [class_a, class_b, class_c]


# Create the box plot
fig, ax = plt.subplots(figsize=(10, 6))
box_plot = ax.boxplot(data, labels=['Class A', 'Class B', 'Class C'],
patch_artist=True)

# Customize the box plot colors
colors = ['lightblue', 'lightgreen', 'lightpink']
[box_plot['boxes'][i].set_facecolor(colors[i]) for i in range(len(colors))]


# Set labels and title
ax.set_xlabel('Classes')
ax.set_ylabel('Exam Scores')
ax.set_title('Comparison of Exam Scores Across Classes')


# Add grid lines for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)


# Display the plot
plt.tight_layout()
plt.show()
