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
MostActiveMarketValues = soup.find_all("div", class_ = "YMlKec")
MostActiveCompanyChanges = soup.find_all("path")
MostActivePercentages = soup.find_all("div", class_ = "JwB6zf")

MostActiveCompanyNames_List = []
MostActiveMarketValues_List = []
MostActivePercentages_List = []
MostActiveCompanyChanges_List = []


for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValues[10: 10 + len(MostActiveCompanyNames_List)]:
    MostActiveMarketValues_List.append(money.text)

for percentage in MostActivePercentages[10 : 10 + len(MostActiveCompanyNames_List)]:
    MostActivePercentages_List.append(percentage.text)

for colour in MostActiveCompanyChanges:
    if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
        MostActiveCompanyChanges_List.append("Down By ")
    elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
        MostActiveCompanyChanges_List.append("Up By ")

MostActiveCompanyChanges_List = MostActiveCompanyChanges_List[10: 10 + len(MostActiveCompanyNames_List)]

for i in range(len(MostActiveCompanyNames_List)):
    MostActivePercentages_List[i] = MostActiveCompanyChanges_List[i] + MostActivePercentages_List[i]

MostActive_DataFrame = pd.DataFrame({"Most Active Company Names": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValues_List, "Change Percentage": MostActivePercentages_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))

print(MostActive_DataFrame)

