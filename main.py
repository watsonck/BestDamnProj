import csv
import sys
from numpy import *

def elecinfo(fname):
    txt = open('can_votes.txt', 'w')
    with open(fname,"r") as fitem:
        filereader = csv.reader(fitem)
        info = []
        next(filereader)
        for line in filereader:
             info.append([line[5],line[6],line[9]])
    return info

def rembad(oldlst):
    newlst = []
    for line in oldlst:
        if line[1] != '':
            newlst.append(line)
            int(newlst[[0]])
    return newlst

def formatdata(oldlst):
    ...

def dictMaker():
    ...

#TODO create decorator add all democrat, republican and independent votes per locality

info19 = elecinfo("2019NovGen.csv")
info18 = elecinfo("2018NovGen.csv")
info17 = elecinfo("2017NovGen.csv")
info16 = elecinfo("2016NovGen.csv")

format16 = rembad(info16)
fil = open("regfile16.txt", "w")
#for line in format16:
    #print(line, file = fil)
print(format16, file= fil)
