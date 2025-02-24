#Team Pooper
#pip3 install pandas --upgrade
#pip3 install matplotlib --upgrade
#Total, Same County, Same Stated different County, Different State, Abroad
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

csvFile = pd.read_csv("data.csv")
table = csvFile[46:54]
povertyData = csvFile[56:60]
homeOwnerData = csvFile[61:64]

total = "United States!!Total!!Estimate"

sCounty ="United States!!Moved; within same county!!Estimate"
dCounty ="United States!!Moved; from different county, same state!!Estimate"
dState = "United States!!Moved; from different  state!!Estimate"
abroad = "United States!!Moved; from abroad!!Estimate"


categories = [

    {
        "name":"United States!!Moved; within same county!!Estimate",
        "title":"Moving Within County in United States by Wealth Bracket",
        "legend":"Yearly Income - People"
    },
    {
        "name":"United States!!Moved; from different county, same state!!Estimate",
        "title":"Moving Within State (different county) in United States by Wealth Bracket",
        "legend":"Yearly Income - People"
    },
    {
        "name":"United States!!Moved; from different  state!!Estimate",
        "title":"Moving out of State in United States by Wealth Bracket",
        "legend":"Yearly Income - People"
    },
    {
        "name":"United States!!Moved; from abroad!!Estimate",
        "title":"Moving from Abroad to United States by Wealth Bracket",
        "legend":"Yearly Income - People"
    }
]

groups = []
for (index, value) in enumerate(table["Label (Grouping)"]):
    groups.append(value.replace('to','-')[8:])

def pieChart(data, title, lTitle, pieLabels):
    # plt.figure(figsize=[8,6], layout='constrained')
    legendLabels = [] 
    labelNumbers = labelNums(data)
    if lTitle == "Poverty Status - People":
        groupsPoverty = []
        for (index, value) in enumerate(povertyData["Label (Grouping)"]):
            groupsPoverty.append(value)
        for index, value in enumerate(groupsPoverty):
            legendLabels.append(f"{value}  |  {labelNumbers[index]}")
        plt.pie(data)
        plt.legend(labels=legendLabels,loc="upper center", title=lTitle, framealpha=.5)
        fig = plt.gcf()
        fig.set_size_inches(8,4)
    elif lTitle == "Home Ownership - People":
        groupsHomeOwners = []
        for (index, value) in enumerate(homeOwnerData["Label (Grouping)"]):
            groupsHomeOwners.append(value)
        for index, value in enumerate(groupsHomeOwners):
            legendLabels.append(f"{value}  |  {labelNumbers[index]}")
        plt.pie(data)
        plt.legend(labels=legendLabels,loc="upper center", title=lTitle, framealpha=.5)
        fig = plt.gcf()
        fig.set_size_inches(8,4)
    elif title == "Combined Moving of United States by Wealth Bracket":
        for index, value in enumerate(groups):
            legendLabels.append(f"{value}  |  {labelNumbers[index]}")
        plt.pie(data)
        plt.legend(labels=legendLabels,loc="center right", title=lTitle, framealpha=.5, bbox_to_anchor=(2,0.5))
        fig = plt.gcf()
        fig.set_size_inches(7,4)
    else:
        for index, value in enumerate(groups):
            legendLabels.append(f"{value}  |  {labelNumbers[index]}")
        plt.pie(data, labels=list(pieLabels), labeldistance=.7)
        plt.legend(labels=legendLabels,loc="center right", title=lTitle, framealpha=.5, bbox_to_anchor=(2,0.5))
        fig = plt.gcf()
        fig.set_size_inches(7,4)
        
    # plt.legend(labels=legendLabels,loc="center right", title=lTitle, framealpha=.5, bbox_to_anchor=(2,0.5))
    plt.title(title, loc="left")
    # fig = plt.gcf()
    # fig.set_size_inches(7,4)
    fileName = title + ".png"
    plt.savefig(fileName, bbox_inches="tight", dpi=200)
    # plt.show()
    plt.clf()
    
def percToFloat(perc):
    result = []

    for i in perc:
        result.append(float(i.strip('%')))
    return result

def percToPop(perc, totals):
    test = []
    totalList = []

    for i in totals:
        totalList.append(i)

    for value, i in enumerate(perc):
        temp = float(i.strip('%')) / 100
        test.append(temp*float(totalList[value].replace(',','')))

    return test

def labelNums(numList):
    newList = []
    for (index, value) in enumerate(numList):
        temp = int('{:.0f}'.format(value))
        newList.append('~'+ '{:,}'.format(temp))
    return newList

for value in categories:
    temp = percToPop(table[value['name']], table[total])
    pieChart(temp, value['title'], value['legend'], table[value['name']])

combined = []
for i in table[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Wealth Bracket", "Yearly Income - People", [])

combined = []
for i in povertyData[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Poverty Status", "Poverty Status - People", [])

combined = []
for i in homeOwnerData[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Home Ownership", "Home Ownership - People", [])