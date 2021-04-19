import json
# Explore the structure of the data.
filename = 'data\eq_data_1_day_m1.json'


def testing_json_files():
    with open(filename) as f:
        all_eq_data = json.load(f)

    all_eq_dicts = all_eq_data['features']
    mags, lons, lats = [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)

    print(len(all_eq_dicts))
    print(mags[:10])    # We print the first 10 to check we're getting the correct data.
    print(lons[:5])
    print(lats[:5])

    # readable_file = 'data\/readable_eq_data.json'
    # with open(readable_file, 'w') as f:
    #     json.dump(all_eq_data, f, indent=4)

# Uncomment the code below to run the script
#testing_json_files()