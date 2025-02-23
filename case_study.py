#Team Pooper
#pip3 install pandas --upgrade
#pip3 install matplotlib --upgrade
#Total, Same County, Same Stated different County, Different State, Abroad
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

csvFile = pd.read_csv("data.csv")
table = csvFile[46:54]

total = "United States!!Total!!Estimate"

sCounty ="United States!!Moved; within same county!!Estimate"
dCounty ="United States!!Moved; from different county, same state!!Estimate"
dState = "United States!!Moved; from different  state!!Estimate"
abroad = "United States!!Moved; from abroad!!Estimate"


categories = [

    {
        "name":"United States!!Moved; within same county!!Estimate",
        "title":"Moving Within County in United States by Wealth Bracket",
        "legend":"Yearly Income"
    },
    {
        "name":"United States!!Moved; from different county, same state!!Estimate",
        "title":"Moving Within State (different county) in United States by Wealth Bracket",
        "legend":"Yearly Income"
    },
    {
        "name":"United States!!Moved; from different  state!!Estimate",
        "title":"Moving out of State in United States by Wealth Bracket",
        "legend":"Yearly Income"
    },
    {
        "name":"United States!!Moved; from abroad!!Estimate",
        "title":"Moving from Abroad to United States by Wealth Bracket",
        "legend":"Yearly Income"
    }
]

groups = []
for (index, value) in enumerate(table["Label (Grouping)"]):
    groups.append(value.replace('to','-')[8:])

def pieChart(data, title, lTitle, pieLabels):
    # plt.figure(figsize=[8,6], layout='constrained')
    legendLabels = []
    labelNumbers = labelNums(data)
    for index, value in enumerate(groups):
        legendLabels.append(f"{value}  |  {labelNumbers[index]}")
    if title == "Combined Moving of United States by Wealth Bracket":
        plt.pie(data)
    else:
        plt.pie(data, labels=list(pieLabels), labeldistance=.7)
        print("yes")
    plt.legend(labels=legendLabels,loc="center right", title=lTitle, framealpha=.5, bbox_to_anchor=(2,0.5))
    plt.title(title, loc="left")
    fig = plt.gcf()
    fig.set_size_inches(7,4)
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
pieChart(list(combined), "Combined Moving of United States by Wealth Bracket", "Yearly Income", [])


# temp = percToPop(table[categories[0]['name']], table[total])
# pieChart(temp, categories[0]['title'], categories[0]['legend'])

# test = pd.DataFrame(data=percToFloat(table[sCounty]))

# test = percToPop(table[sCounty], table[total])

# pieChart(test, "Pie Chart", "Legend")

# plt.pie(test, labels=test)
# plt.legend(labels=table[group],loc="upper right", title="test")
# plt.title("Title")
# plt.show()
# plt.savefig("figure.png")
# plt.clf()

# test = percToFloat(table[sCounty])

# plt.pie(test, labels= test)
# plt.legend(labels=table[group],loc="upper right")
# plt.show()
# plt.savefig("figure2.png")

# test.plot(kind="hist", color="red")
# plt.ylabel("Percent of people (%)")
# plt.xlabel("Wealth Brackets")
# plt.xticks(barX,table[group])
# plt.tick_params(axis="x", labelrotation=0)
# plt.text()

# table2.plot(kind="hist", alpha=0.4)
# plt.show()