#Team Pooper
#pip3 install pandas --upgrade
#pip3 install matplotlib --upgrade
#Total, Same County, Same Stated different County, Different State, Abroad
import pandas as pd
import matplotlib.pyplot as plt

table2 = pd.read_csv("data.csv")
table = table2[46:54]

total = "United States!!Total!!Estimate"

sCounty ="United States!!Moved; within same county!!Estimate"
dCounty ="United States!!Moved; from different county, same state!!Estimate"
dState = "United States!!Moved; from different  state!!Estimate"
abroad = "United States!!Moved; from abroad!!Estimate"

groups = []
for (index, value) in enumerate(table["Label (Grouping)"]):
    groups.append(value.replace('to','-')[8:])
print(groups)
# barX = [0, 1, 2, 3, 4, 5, 6, 7]
# print(table)
# print(table[sCounty])

def pieChart(data, title, lTitle):
    
    plt.pie(data, labels=labelNums(data))
    plt.legend(labels=groups,loc="upper right", title=lTitle)
    plt.title(title)
    plt.show()
    fileName = title + ".png"
    plt.savefig(fileName)
    plt.clf()
    


def percToFloat(perc):
    test = []

    for i in perc:
        test.append(float(i.strip('%')))
    return test

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
# test = pd.DataFrame(data=percToFloat(table[sCounty]))

test = percToPop(table[sCounty], table[total])

# Note in case I forgor bc adhd: reviewing the certifications idk if we even want bar charts. 
# A scatter could also work 
# or we could find a way to get everything onto one histogram with $ brackets color coded


pieChart(test, "Pie Chart", "Legend")

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
