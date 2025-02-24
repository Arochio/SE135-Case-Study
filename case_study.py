#Team Pooper
#pip3 install pandas --upgrade
#pip3 install matplotlib --upgrade

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Initialize The Tables
csvFile = pd.read_csv("data.csv")
wealthData = csvFile[46:54]
povertyData = csvFile[57:60]
homeOwnerData = csvFile[62:64]

# Dictionary for iterating over the main wealthData
total = "United States!!Total!!Estimate"
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

# Legend Labels
groups = []
for (index, value) in enumerate(wealthData["Label (Grouping)"]):
    groups.append(value.replace('to','-')[8:])


# This function builds the pie charts
def pieChart(data, title, lTitle, pieLabels=[]):
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
    plt.show()
    plt.clf()
    
# This function trips the % from a string and casts it as a float
def percToFloat(perc):
    
    result = []

    for i in perc:
        result.append(float(i.strip('%')))
    return result

# Calculates raw number of people for charting by stripping commas, %s, and multiplying % by totals
def percToPop(perc, totals):
    test = []
    totalList = []

    for i in totals:
        totalList.append(i)

    for value, i in enumerate(perc):
        temp = float(i.strip('%')) / 100
        test.append(temp*float(totalList[value].replace(',','')))

    return test

# Formats numbers for the legend
def labelNums(numList):

    newList = []

    for (index, value) in enumerate(numList):
        temp = int('{:.0f}'.format(value))
        newList.append('~'+ '{:,}'.format(temp))

    return newList


# ---------------------Main Code------------------------
#Moving by wealth - sub categories
for value in categories:
    temp = percToPop(wealthData[value['name']], wealthData[total])
    pieChart(temp, value['title'], value['legend'], wealthData[value['name']])

# Moving by wealth - combined
combined = []
for i in wealthData[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Wealth Bracket", "Yearly Income - People")

# Moving by poverty status
combined = []
for i in povertyData[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Poverty Status", "Poverty Status - People")

# moving by home ownership
combined = []
for i in homeOwnerData[total]:
    combined.append(float(i.replace(',','')))
pieChart(list(combined), "Combined Moving of United States by Home Ownership", "Home Ownership - People")