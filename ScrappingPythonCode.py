import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get(
    "https://weather.com/en-IN/weather/tenday/l/a5f0fe2ff9a40acc9ce62d67cd99439a71cde78cc0c5c1fbf6da052bef4cdba9")
soup = BeautifulSoup(r.text, "html.parser")

d=[]
date = soup.find_all('span', class_="DailyContent--daypartDate--3VGlz")
for i in range(10):
    d.append(date[i].text)
    print(date[i].text)

ht=[]
high_temp = soup.find_all('span', class_="DetailsSummary--highTempValue--3PjlX")
for j in range(10):
    ht.append(high_temp[j].text)
    print(high_temp[j].text)

lt=[]
low_temp = soup.find_all('span', "DetailsSummary--lowTempValue--2tesQ")
for h in range(10):
    lt.append(low_temp[h].text)
    print(low_temp[h].text)

wc=[]
weather_condition = soup.find_all('div', class_="DetailsSummary--condition--2JmHb")
for k in range(10):
    wc.append(weather_condition[k].text)
    print(weather_condition[k].text)

rp=[]
rain_percentage=soup.find_all('span', class_="DailyContent--value--1Jers")
#rain_percentage = soup.find_all("tag,{Data_test-id:value}")
for f in range(10):
    a = rain_percentage[f].text
    rp.append(a)
    print(a)

ws=[]
wind_speed = soup.find_all('span',
                           class_="Wind--windWrapper--3Ly7c DailyContent--value--1Jers DailyContent--windValue--JPpmk")
for c in range(10):
    x=wind_speed[c].text.split()[1]
    ws.append(x)
    print(x)
wd=[]
wind_direction = soup.find_all('span',
                               class_="Wind--windWrapper--3Ly7c DailyContent--value--1Jers DailyContent--windValue--JPpmk")
for d in range(10):
    wd.append(wind_direction[d].text)
    print(wind_direction[d].text.split()[0])

col={'date': d,'high_temp':ht,'low_temp':lt,'weather_condition':wc,'rain_percentage':rp,'wind_speed':ws,'wind_direction':wd}
Dataframe=pd.DataFrame(col)
print(Dataframe)
Dataframe.to_csv("weatherReport.csv")
