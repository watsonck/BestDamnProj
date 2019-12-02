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

def dictMaker(oldlst):
    newdict = {}
    for el in oldlst:
        newdict.update({(el[1],el[2]) : el[0]})
                
    return newdict
        
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



        
#infofil = open('can_votes.txt','w')


#for i in range(0,len(info16)-1):
#    print(info16[i], file = infofil)
#infofil.close()
