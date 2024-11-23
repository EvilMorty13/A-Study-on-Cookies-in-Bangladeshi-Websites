import os
import time
import pandas as pd
import re
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Manually add your csv file here
sheet_id = "1aht9oOanM1SeiZABuaLCb7079ZnynICzqGxpKIW6_Kc"

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

firstNecessary = 0
firstFunctionality = 0
firstAnalytics = 0
firstAdvertising = 0

thirdNecessary = 0
thirdFunctionality = 0
thirdAnalytics = 0
thirdAdvertising = 0

dmCollection = []
label = ['"current_label": 0,', '"current_label": 1,', '"current_label": 2,', '"current_label": 3,']
w1 = "www."
w2 = "https://"
w3 = "http://"
for url in df["URL"]:
    if w1 in url:
        dm = url.split("www.")[-1].split("/")[0]
        dm = '"' + dm + '"'
        dmCollection.append(dm)
    elif w2 in url:
        dm = url.split("https://")[-1].split("/")[0]
        dm = '"' + dm + '"'
        dmCollection.append(dm)
    elif w3 in url:
        dm = url.split("http://")[-1].split("/")[0]
        dm = '"' + dm + '"'
        dmCollection.append(dm)

ff = 1
for t in dmCollection:
    ff += 1
    print(t + "  " + str(ff))



f = (open("../cookies/gov.txt", "r"))

for x in f:
    if any(dm in x for dm in dmCollection):
        for x_new in f:
            if label[0] in x_new:
                firstNecessary += 1
            if label[1] in x_new:
                firstFunctionality += 1
            if label[2] in x_new:
                firstAnalytics += 1
            if label[3] in x_new:
                firstAdvertising += 1

            if re.match(r'    },', x_new):
                break
    else:
        if label[0] in x:
            thirdNecessary += 1
        if label[1] in x:
            thirdFunctionality += 1
        if label[2] in x:
            thirdAnalytics += 1
        if label[3] in x:
            thirdAdvertising += 1


totalWebsite = len(dmCollection)
firstTotal = firstNecessary+firstFunctionality+firstAnalytics+firstAdvertising
thirdTotal = thirdNecessary+thirdFunctionality+thirdAnalytics+thirdAdvertising
totalNecessary = firstNecessary+thirdNecessary
totalFunctionality = firstFunctionality+thirdFunctionality
totalAnalytics = firstAnalytics+thirdAnalytics
totalAdvertising = firstAdvertising+thirdAdvertising
totalCookies = firstTotal+thirdTotal


print()
print("Website Visited : " +str(totalWebsite))
print()
print("1st party cookies(Necessary) : " + str(firstNecessary))
print("1st party cookies(Functionality) : "+ str(firstFunctionality))
print("1st party cookies(Analytics) : "+str(firstAnalytics))
print("1st party cookies(Advertising) : "+str(firstAdvertising))
print("Total 1st party cookies : " + str(firstTotal))
print()
print("3rd party cookies(Necessary) : "+str(thirdNecessary))
print("3rd party cookies(Functionality) : "+str(thirdFunctionality))
print("3rd party cookies(Analytics) : "+str(thirdAnalytics))
print("3rd party cookies(Advertising) : "+str(thirdAdvertising))
print("Total 3rd party cookies : " + str(thirdTotal))
print()
print("Total Cookies(Necessary) : "+str(totalNecessary))
print("Total Cookies(Functionality) : "+str(totalFunctionality))
print("Total Cookies(Analytics) : "+str(totalAnalytics))
print("Total Cookies(Advertising) : "+str(totalAdvertising))
print("Total Cookies : "+str(totalCookies))



# Plotting the graph
labels = ['Necessary', 'Functionality', 'Analytics', 'Advertising']
first_party = [firstNecessary, firstFunctionality, firstAnalytics, firstAdvertising]
third_party = [thirdNecessary, thirdFunctionality, thirdAnalytics, thirdAdvertising]

x = range(len(labels))  # The x locations for the groups
width = 0.35  # The width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, first_party, width, label='1st Party Cookies', color='#375E97')
rects2 = ax.bar([i + width for i in x], third_party, width, label='3rd Party Cookies', color='#FB6542')

# Adding some text for labels, title and axes ticks
ax.set_ylim(0, max(max(first_party), max(third_party)) * 1.1)
ax.set_xlabel('Cookie Type')
ax.set_ylabel('Number of Cookies')
ax.set_title('Total Government Website Visited : ' + str(totalWebsite))
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(labels)
ax.legend()


# Adding the values above the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

# Save the figure
results_folder = '../results'  # One step back from the current working directory
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
fig.savefig(os.path.join(results_folder, 'gov.png'), format='png')

plt.show()