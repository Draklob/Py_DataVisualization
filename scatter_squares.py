import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)  # Set title to X label
plt.ylabel("Square of Value", fontsize=14)  # Set title to Y label

# Set chart title and label axes.
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
# plt.savefig('squares_plot.png', bbox_inches='tight')    # Save a png photo without whitespace from plot.
plt.show()
