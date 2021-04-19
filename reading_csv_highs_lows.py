import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2018_simple.csv'
filename = 'sitka_weather_2018_simple.csv'
# filename = 'rdu-weather-history.csv'
dates, highs, lows = [], [], []


def reading_data():
    with open(filename) as f:   # IMPORTANT: After the with: the file is closed and it can't be read anything else.
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        # An example how to read the csv file by getting the core values of the csv from the first line
        # for index, column_header in enumerate(header_row):  # We use enumerate to get index and value like a dictionary
        #     print(index, column_header)
        # 0    STATION
        # 1    NAME
        # 2    DATE
        # 3    PRCP
        # 4    TAVG
        # 5    TMAX
        # 6    TMIN

        # Get high temperatures from file
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Getting lines/columns from the file
# columns = []
# for column in reader:
#     print(column)

def drawing_plot():
    # Plot data.
    # fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.style.use('seaborn')
    fig, ax = plt.subplots(dpi=128, figsize=(10, 6))
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.plot(dates, highs, c='red')
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high temperatures, 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # To draw the date labels diagonally to prevent them from overlapping.
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('temperatures.png', bbox_inches='tight')  # Save a png photo without whitespace from plot.
    plt.show()

def run_script():
    reading_data()
    drawing_plot()
    #print(highs)