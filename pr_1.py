from apriori_python import apriori
import csv
from pprint import pprint


with open("assoc.csv", "r", encoding="utf-8") as f:
    data = list(csv.reader(f))

objects = data[0]

def map_transaction(norm, objects):
    t = []
    for i, value in enumerate(norm):
        if int(value):
            t.append(objects[i])
    return t

transations = [map_transaction(x, objects) for x in data[1:]]

pprint(transations)


