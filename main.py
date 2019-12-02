import csv
import sys
from numpy import *

#Takes in NovGen16-19 files and filters out the info we dont care about
def elecinfo(fname):
    with open(fname,"r") as fitem:
        filereader = csv.reader(fitem)
        info = []
        next(filereader)
        for line in filereader:
            if line[5] != '' and line[6] != '':
                line[5] = int(line[5])
                info.append([line[5],line[6],line[9]])
    return info

#Makes the dictionary and adds votes to the map if the key is the same
def dictMaker(oldlst):
    newdict = {}
    for el in oldlst:
        #if (el[1],el[2]) in newdict:
            #newdict[(el[1],el[2])] += el[0]
        #else:
            #newdict.update({(el[1],el[2]) : el[0]})
        if el[1] in newdict:
            newdict[el[1]] += el[0]
        else:
            newdict.update({el[1]:el[0]})   
    return newdict
        
#Makes file for the dictionary
def fileMaker(lst, fil):
    ofil = open(fil,'w')
    print(lst,file=ofil)
    ofil.close()



info19 = elecinfo("2019NovGen.csv")
info18 = elecinfo("2018NovGen.csv")
info17 = elecinfo("2017NovGen.csv")
info16 = elecinfo("2016NovGen.csv")

format16 = dictMaker(info16)
format17 = dictMaker(info17)
format18 = dictMaker(info18)
format19 = dictMaker(info19)

toGraph16 = fileMaker(format16, 'regfile16.txt')
toGraph17 = fileMaker(format17, 'regfile17.txt')
toGraph18 = fileMaker(format18, 'regfile18.txt')
toGraph19 = fileMaker(format19, 'regfile19.txt')



        
infofil = open('can_votes.txt','w')


for i in range(0,len(info16)-1):
    print(info16[i], file = infofil)
infofil.close()
