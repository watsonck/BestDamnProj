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
            if line[5] != '' and line[6] != '':
                line[5] = int(line[5])
                info.append([line[5],line[6],line[9]])
    return info
#added line 20 to the first for loop
'''
def rembad(oldlst):
    newlst = []
    for line in oldlst:
        if line[1] != '':
            newlst.append(line)
            int(newlst[[0]])
    return newlst
'''

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def dictMaker(oldlst):
    newdict = {}
    for el in oldlst:
        newdict.update({(el[1],el[2]) : el[0]})
         
                
    return newdict
        




#TODO create decorator add all democrat, republican and independent votes per locality

info19 = elecinfo("2019NovGen.csv")
info18 = elecinfo("2018NovGen.csv")
info17 = elecinfo("2017NovGen.csv")
info16 = elecinfo("2016NovGen.csv")

format16 = dictMaker(info16)
fil = open("regfile16.txt", "w")
print(format16, file=fil)
fil.close()
        
infofil = open('can_votes.txt','w')


for i in range(0,len(info16)-1):
    print(info16[i], file = infofil)
infofil.close()
