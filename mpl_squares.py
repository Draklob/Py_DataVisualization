import matplotlib.pyplot as plt  # pyplot contains a number of functions that help generate chars and plots.

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]  # list to pass it tot he plot ft
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)  # make the line thicker, controls the thickness of the line

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)  # Set title for the chart and size of the font.
plt.xlabel("Value", fontsize=14)  # Set title to X label
plt.ylabel("Square of Value", fontsize=14)  # Set title to Y label

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()
