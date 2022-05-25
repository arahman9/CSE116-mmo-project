import json
import csv


def csvtoarray():
    result = []
    with open("grid.csv", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            result.append(line)
    return json.dumps(result)