import csv
import sys

def elecinfo():
    txt = open('can_votes.txt', 'w')
    with open('2019NovGen.csv', "r") as fitem:
        filereader = csv.reader(fitem)
        for line in filereader:
            print(line[5],line[6],line[9], file = txt)
        


#TODO create decorator add all democrat, republican and independent votes per locality
