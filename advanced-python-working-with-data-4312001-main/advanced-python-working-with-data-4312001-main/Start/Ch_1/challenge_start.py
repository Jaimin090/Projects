# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
def isaQuake(q):
    return q["properties"]["type"] == "earthquake"
# filter out non-earthquake entries from the data
quakes = list(filter(isaQuake, data["features"]))
# part 1: how many total quakes?
total_quakes = len(quakes)
print(f"\nTotal number of Earthquakes: {total_quakes}\n")