import csv
import sys

result = []
txt = open('can_votes.txt', 'w')
with open('2019electionsum.csv', "r") as fitem:
    filereader = csv.reader(fitem)
    for line in filereader:
        print(line[9],line[10],line[20], file = txt)
    #print(result[9],result result[total_votes])
        #print(line[9],line[10],line[17],line[20])
        
