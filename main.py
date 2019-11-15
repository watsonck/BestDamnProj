import csv
import sys

result = []
with open(file name, "r") as fitem:
    filereader = csv.reader(fitem)
    for line in filereader:
        result.append(line)

    print(result)
