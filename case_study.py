#Team Pooper
#pip3 install pandas --upgrade
#pip3 install matplotlib --upgrade
#Total, Same County, Same Stated different County, Different State, Abroad
import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv("data.csv")[46:54]

total = "United States!!Total!!Estimate"
sCounty ="United States!!Moved; within same county!!Estimate"
dCounty ="United States!!Moved; from different county, same state!!Estimate"
dState = "United States!!Moved; from different  state!!Estimate"
abroad = "United States!!Moved; from abroad!!Estimate"
group = "Label (Grouping)"

barX = [0, 1, 2, 3, 4, 5, 6, 7]

print(table)
print(table[sCounty])

def percToFloat(perc):
    test = []

    for i in perc:
        test.append(float(i.strip('%')))
    return test


test = pd.DataFrame(data=percToFloat(table[sCounty]))

print(test)

test.plot(kind="bar")
plt.ylabel("Percent of people (%)")
plt.xlabel("Wealth Brackets")
plt.xticks(barX,table[group])
plt.tick_params(axis="x", labelrotation=0)
plt.text()
plt.show()