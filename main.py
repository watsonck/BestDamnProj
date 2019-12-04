import csv
import sys
#from numpy import *
import matplotlib.pyplot as plt
import numpy as np

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

print(format19)
print(format18)
print(format17)
print(format16)

#making graphs

labels19 = ['Independent','Republican','Democratic','Write-In','Libertarian']
values19 = [format19['Independent'],format19['Republican'],format19['Democratic'],format19['Write-In'],format19['Libertarian']]

index = np.arange(len(labels))
plt.bar(index19 values19)
plt.xlabel("political party")
plt.ylabel("# of votes")
plt.xticks(index19, labels19)
plt.title("2019 party comparison")
plt.show()
'''
labels18 = ['Independent','Republican','Democratic','Libertarian','Write-In']
values18 = [format18['Independent'],format18['Republican'],format18['Democratic'],format18['Libertarian'],format18['Write-In']]

index18 = np.arange(len(labels18))
plt.bar(index, values)
plt.xlabel("political party")
plt.ylabel("# of votes")
plt.xticks(index, labels)
plt.title("2019 party comparison")
plt.show()

'''
