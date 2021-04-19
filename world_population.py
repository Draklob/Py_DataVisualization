import json

def run_world_population():
    # Load the data into a list. We should make a catch statement to sure the file exists, but not for simple example.
    # We could create a function with a parameter to read a specific file.
    filename ='population_data.json'
    with open(filename) as f:
        pop_data = json.load(f)

    # Print the 2010 population for each country.
    for pop_dict in pop_data:
        if pop_dict['Year'] == 2010:
            country_name = pop_dict['Country Name']
            population = int(pop_dict['Value'])
            print(f"{country_name} has: {str(population)}")