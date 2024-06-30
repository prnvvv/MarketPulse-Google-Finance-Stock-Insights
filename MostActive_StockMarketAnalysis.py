import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/markets/most-active"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

MostActiveCompanyNames = soup.find_all("div", class_ = "ZvmM7")
MostActiveMarketValue = soup.find_all("div", class_ = "YMlKec")
MostActivePercentage = soup.find_all("path")

MostActiveCompanyNames_List = []
MostActiveMarketValue_List = []
MostActivePercentage_List = []
MostActiveChangeValue_List = []

for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValue[10: 10+len(MostActiveCompanyNames_List)]:
    MostActiveMarketValue_List.append(money.text)

for i in MostActivePercentage:
    if i["d"]:
        if i["d"] == "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
            ChangeValue = "Down By "
            MostActiveChangeValue_List.append(ChangeValue)
        elif i["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
            ChangeValue = "Up by "
            MostActiveChangeValue_List.append(ChangeValue)
    else:
        MostActiveChangeValue_List.append("No Change")

#MostActive_DataFrame = pd.DataFrame({"Gainer Company Names": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValue_List, "Increase Percentage": MostActivePercentage_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))

MostActiveChangeValue_List = MostActiveChangeValue_List[10: 59]
print(len(MostActiveChangeValue_List))
print(len(MostActiveCompanyNames_List))
print(len(MostActiveMarketValue_List))

