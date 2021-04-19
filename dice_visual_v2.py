from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def run_test():
    # Create a D6
    die_1 = Die()
    die_2 = Die()

    #Make some rolls, and store results in a list.
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    # Plotly doesnt accept the results of range function directly, so we need to convert the range to a list explicitly.
    x_values = list(range(2, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1} # dtick 1 tells Plotly to label every tick mark.
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of rolling two D6 1000 times',
                       xaxis=x_axis_config, yaxis=y_axis_config)
    # This function needs a dictionary containing the data and layout objects.
    # Also accepts a name for the file where will be saved.
    offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')