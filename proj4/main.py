import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


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

#Creates a list of filtered info from csv files    
info19 = elecinfo("data/2019NovGen.csv")
info18 = elecinfo("data/2018NovGen.csv")
info17 = elecinfo("data/2017NovGen.csv")
info16 = elecinfo("data/2016NovGen.csv")

#Gather user input
print("what year would you like? [all][2019][2018][2017][2016]")
year = input()
print("State or locatality? [state][###]")
area = input()

if year == 'all' and area != 'state':
    print("Grouped or stacked? [group][stack]")
    gors = input()


#if they want all the years of the state----------------------------------------
#Animated bar chart---------------------------------------------------------------
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

    fig, ax = plt.subplots() 


    def drawBar(year):
        ax.clear()
        if str(year) == '2019':
            val = value19
            #print("h1")
        if str(year) == '2018':
            val = value18
            #print("h2")
        if str(year) == '2017':
            val = value17
            #print("h3")
        if str(year) == '2016':
            val = value16
            #print("h4")
        x = np.arange(7)
        width = .2

        leg1 = ax.barh(x, val, width,color= ['red', 'blue', 'gray', 'green', 'yellow', 'black'], label =year)

        ax.set_ylabel('Parties')
    
        ax.set_title('Virginia Party votes through '+str(year))
        ax.set_yticks(x)
        ax.set_yticklabels(labels, fontsize = 10)
        ax.legend()

    animation = animation.FuncAnimation(fig, drawBar, repeat = True, frames = range(2016,2020))
    plt.show()
    plt.close()

    '''
    x = np.arange(7)
    width = .1


    fig, ax = plt.subplots()
    leg1 = ax.barh(x - width, value16, width, label ='2016')
    leg2 = ax.barh(x, value17, width, label ='2017')
    leg3 = ax.barh(x + width, value18, width, label ='2018')
    leg4 = ax.barh(x + 2*width, value19, width, label ='2019')

    ax.set_ylabel('Parties')
    
    ax.set_title('Virginia Party votes through the Year')
    ax.set_yticks(x)
    ax.set_yticklabels(labels, fontsize = 10)
    ax.legend()
    plt.show()
    '''



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
        fig1, ax = plt.subplots()
        ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        ax.axis('equal')
        plt.show()
 
    #2019---------------------------------------------------------------------------
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
        fig1, ax = plt.subplots()
        ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
        ax.axis('equal')
        plt.show()
 
    #2019---------------------------------------------------------------------------
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
        fig1, ax = plt.subplots()
        ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
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
        fig1, ax = plt.subplots()
        ax.pie(val, labels = labels, autopct = '%1.1f%%',shadow = False, startangle= 0)
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


    if gors == 'group':
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

    if gors == 'stack':
        x = np.arange(7)
        width = 1
        val = np.add(value16,value17)
        val2 = np.add(value18,val)


        fig, ax = plt.subplots()
        leg1 = ax.bar(x, value16, width, edgecolor = 'white', label ='2016')
        leg2 = ax.bar(x, value17, width, edgecolor = 'white', bottom = value16, label ='2017')
        leg3 = ax.bar(x, value18, width, edgecolor = 'white',bottom = val, label ='2018')
        leg4 = ax.bar(x, value19, width, edgecolor = 'white', bottom = val2, label ='2019')

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
                labels.append(item[0] + '-' +str(format19[item]))
                value.append(format19[item])
        fig1, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(value, autopct = '%1.1f%%',shadow = False, startangle = 0)
        #ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = True, startangle= 0)
        ax.legend(wedges, labels,title = "Parties", loc = 'upper right')
        ax.axis('equal')
        plt.show()

    #2018 ----------------------------------------------------------
    if year == "2018":
        format18 = DictMaker(info18)

        labels = []
        value = []
    
        for item in format18:
            if item[1] == area:
                labels.append(item[0] + '-' +str(format18[item]))
                value.append(format18[item])
        fig1, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(value, autopct = '%1.1f%%',shadow = False, startangle = 0)
        #ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = True, startangle= 0)
        ax.legend(wedges, labels,title = "Parties", loc = 'upper right')
        ax.axis('equal')
        plt.show()

    #2017 ----------------------------------------------------------
    if year == "2017":
        format17 = DictMaker(info17)

        labels = []
        value = []
    
        for item in format17:
            if item[1] == area:
                labels.append(item[0] + '-' +str(format17[item]))
                value.append(format17[item])
        fig1, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(value, autopct = '%1.1f%%',shadow = False, startangle = 0)
        #ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = True, startangle= 0)
        ax.legend(wedges, labels,title = "Parties", loc = 'upper right')
        ax.axis('equal')
        plt.show()

    #2016 ----------------------------------------------------------
    if year == "2016":
        format16 = DictMaker(info16)

        labels = []
        value = []
    
        for item in format16:
            if item[1] == area:
                labels.append(item[0] + '-' +str(format16[item]))
                value.append(format16[item])
        fig1, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(value, autopct = '%1.1f%%',shadow = False, startangle = 0)
        #ax.pie(value, labels = labels, autopct = '%1.1f%%',shadow = True, startangle= 0)
        ax.legend(wedges, labels,title = "Parties", loc = 'upper right')
        ax.axis('equal')
        plt.show()
      
