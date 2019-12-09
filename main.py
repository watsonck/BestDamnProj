import csv
import sys
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
def stateDictMaker(oldlst):
    newdict = {}
    for el in oldlst:
        if el[1] in newdict:
            newdict[el[1]] += el[0]
        else:
            newdict.update({el[1]:el[0]})   
    return newdict

#Makes the dictionary and adds votes to the map if the key is the same fo
#for whole state
def DictMaker(oldlst):
    newdict = {}
    for el in oldlst:
        if (el[1],el[2]) in newdict:
            newdict[(el[1],el[2])] += el[0]
        else:
            newdict.update({(el[1],el[2]) : el[0]})
    return newdict
        
info19 = elecinfo("2019NovGen.csv")
info18 = elecinfo("2018NovGen.csv")
info17 = elecinfo("2017NovGen.csv")
info16 = elecinfo("2016NovGen.csv")

#Gather user input
print("what year would you like? [all][2019][2018][2017][2016]")
year = input()
print("State or locatality? [state][###]")
area = input()

infofil = open('can_votes.txt','w')



#if they want all the years of the state
#Stacked bar chart
if year == "all" and area == "state":
    format19 = stateDictMaker(info19)
    format18 = stateDictMaker(info18)
    format17 = stateDictMaker(info17)
    format16 = stateDictMaker(info16)

    overDict = {}
    for item in format19:
        overDict.update({('2019',item):format19[item]})
    for item in format18:
        overDict.update({('2018',item):format18[item]})
    for item in format17:
        overDict.update({('2017',item):format17[item]})
    for item in format16:
        overDict.update({('2016',item):format16[item]})

    labels = ['Republican','Democratic','Independent', 'Green', 'Libertarian','Write-In']
    value19 = [0,0,0,0,0,0,0]
    value18 = [0,0,0,0,0,0,0]
    value17 = [0,0,0,0,0,0,0]
    value16 = [0,0,0,0,0,0,0]

    for item in overDict:
        if item[0] == '2019':
            value19[labels.index(item[1])]= overDict[item]
        if item[0] == '2018':
            value18[labels.index(item[1])]= overDict[item]
        if item[0] == '2017':
            value17[labels.index(item[1])]= overDict[item]
        if item[0] == '2016':
            value16[labels.index(item[1])]= overDict[item]
    
    value19 = np.array(value19)
    value18 = np.array(value18)
    value17 = np.array(value17)
    value16 = np.array(value16)

    x = np.arange(7)
    width = .1


    fig, ax = plt.subplots()
    leg1 = ax.bar(x - width, value16, width, label ='2016')
    leg2 = ax.bar(x, value17, width, label ='2017')
    leg3 = ax.bar(x + width, value18, width, label ='2018')
    leg4 = ax.bar(x + 2*width, value19, width, label ='2019')

    ax.set_ylabel('Votes')
    
    ax.set_title('Virginia Party votes through the Year')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize = 6)
    ax.legend()
    plt.show()




#-----------------------------------------------------------------------------------
#Specific year in the state
#some chart
if year != "all" and area == "state":
    
    #2019---------------------------------------------------------------------------
    if year == "2019":
        format19 = stateDictMaker(info19)
        
        labels = format19.keys()
        val = list(format19.values())
        total = 0
        for item in val:
            total = item + total

        value = []
        for item in val:
            newVal = item/total
            value.append(newVal)
        #fig1, ax = plt.subplots()
        patches, texts = plt.pie(value, shadow = False, startangle = 0)
        #patches, texts =ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()

    #2018---------------------------------------------------------------------------
    if year == "2018":
        format18 = stateDictMaker(info18)
        
        labels = format18.keys()
        val = list(format18.values())
        total = 0
        for item in val:
            total = item + total

        value = []
        for item in val:
            newVal = item/total
            value.append(newVal)
        #fig1, ax = plt.subplots()
        patches, texts = plt.pie(value, shadow = False, startangle = 0)
        #patches, texts =ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()

    #2017---------------------------------------------------------------------------
    if year == "2017":
        format17 = stateDictMaker(info17)
        
        labels = format17.keys()
        val = list(format17.values())
        total = 0
        for item in val:
            total = item + total

        value = []
        for item in val:
            newVal = item/total
            value.append(newVal)
        #fig1, ax = plt.subplots()
        patches, texts = plt.pie(value, shadow = False, startangle = 0)
        #patches, texts =ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()

    #2016---------------------------------------------------------------------------
    if year == "2016":
        format16 = stateDictMaker(info16)
        
        labels = format16.keys()
        val = list(format16.values())
        total = 0
        for item in val:
            total = item + total

        value = []
        for item in val:
            newVal = item/total
            value.append(newVal)
        #fig1, ax = plt.subplots()
        patches, texts = plt.pie(value, shadow = False, startangle = 0)
        #patches, texts =ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()


#-------------------------------------------------------------------
# All years in a Locality
#grouped bar chart
if year == "all" and area != "state":
    format19 = DictMaker(info19)
    format18 = DictMaker(info18)
    format17 = DictMaker(info17)
    format16 = DictMaker(info16)

    overDict = {}

    for item in format19:
        if item[1] == area:
            overDict.update({('2019',item[0],item[1]):format19[item]})
    for item in format18:
        if item[1] == area:
            overDict.update({('2018',item[0], item[1]):format18[item]})
    for item in format17:
        if item[1] == area:
            overDict.update({('2017',item[0],item[1]):format17[item]})
    for item in format16:
        if item[1] == area:
            overDict.update({('2016',item[0],item[1]):format16[item]})

    labels = ['Republican','Democratic','Independent', 'Green', 'Libertarian','Write-In']
    value19 = [0,0,0,0,0,0,0]
    value18 = [0,0,0,0,0,0,0]
    value17 = [0,0,0,0,0,0,0]
    value16 = [0,0,0,0,0,0,0]
    
    for item in overDict:
        if item[0] == '2019':
            value19[labels.index(item[1])]= overDict[item]
        if item[0] == '2018':
            value18[labels.index(item[1])]= overDict[item]
        if item[0] == '2017':
            value17[labels.index(item[1])]= overDict[item]
        if item[0] == '2016':
            value16[labels.index(item[1])]= overDict[item]

 
    value19 = np.array(value19)
    value18 = np.array(value18)
    value17 = np.array(value17)
    value16 = np.array(value16)

    x = np.arange(7)
    width = .1


    fig, ax = plt.subplots()
    leg1 = ax.bar(x - width, value16, width, label ='2016')
    leg2 = ax.bar(x, value17, width, label ='2017')
    leg3 = ax.bar(x + width, value18, width, label ='2018')
    leg4 = ax.bar(x + 2*width, value19, width, label ='2019')

    ax.set_ylabel('Votes')
    
    ax.set_title(str(area)+ 'Party votes through the Year')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize = 6)
    ax.legend()
    plt.show()





#-------------------------------------------------------------------
#Specific year in Locality
#pie Chart
if year != "all" and area != "state":

    #2019----------------------------------------------------------
    if year == "2019":
        format19 = DictMaker(info19)

        labels = []
        value = []
    
        for item in format19:
            if item[1] == area:
                labels.append(item[0])
                value.append(format19[item])
        fig1, ax = plt.subplots()
        #patches, texts = plt.pie(value, shadow = False, startangle = 0)
        ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        #plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()

    #2018 ----------------------------------------------------------
    if year == "2018":
        format18 = DictMaker(info18)

        labels = []
        value = []
    
        for item in format18:
            if item[1] == area:
                labels.append(item[0])
                value.append(format18[item])
        fig1, ax = plt.subplots()
        #patches, texts = plt.pie(value, shadow = False, startangle = 0)
        ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        #plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()
    

    #2017 ----------------------------------------------------------
    if year == "2017":
        format17 = DictMaker(info17)

        labels = []
        value = []
    
        for item in format17:
            if item[1] == area:
                labels.append(item[0])
                value.append(format17[item])
        fig1, ax = plt.subplots()
        #patches, texts = plt.pie(value, shadow = False, startangle = 0)
        ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        #plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()
    
    
    #2016 ----------------------------------------------------------
    if year == "2016":
        format16 = DictMaker(info16)

        labels = []
        value = []
    
        for item in format16:
            if item[1] == area:
                labels.append(item[0])
                value.append(format16[item])
        fig1, ax = plt.subplots()
        #patches, texts = plt.pie(value, shadow = False, startangle = 0)
        ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        #plt.legend(patches, labels, loc = 'best')
        ax.axis('equal')
        plt.show()
      
            
for i in range(0,len(info16)-1):
    print(info16[i], file = infofil)
infofil.close()

