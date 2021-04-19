import pygal

from die import Die


def run_test():
    # Create a D6 and D10
    die_1 = Die()
    die_2 = Die(10)

    #Make some rolls, and store results in a list.
    # Number of throws we want to test for the chart.
    number_throws = 50000
    results = []
    for roll_num in range(number_throws):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    x_label = []
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
        x_label.append(value)

    # Visualize the results.
    hist = pygal.Bar()  # Bar chart
    str_title = f'two D{die_1.num_sides}' if die_1.num_sides == die_2.num_sides else \
        f'D{die_1.num_sides} and D{die_2.num_sides}'
    hist.title = f"Results of rolling {str_title} {number_throws} times."
    hist.x_labels = x_label
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add(f'D{die_1.num_sides} + D{die_2.num_sides}', frequencies)
    hist.render_to_file('different_diceD6_D10.svg')
    #print(frequencies)