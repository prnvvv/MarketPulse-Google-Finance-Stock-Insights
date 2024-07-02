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
MostActiveCompanyChange = soup.find_all("path")

MostActiveCompanyNames_List = []
MostActiveMarketValue_List = []
MostActivePercentage_List = []
MostActiveCompanyChange_List = []


for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValue[10: 10+len(MostActiveCompanyNames_List)]:
    MostActiveMarketValue_List.append(money.text)

for colour in MostActiveCompanyChange[10: 10 + len(MostActiveCompanyNames_List)]:
    if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
        MostActiveCompanyChange_List.append("Down By ")
    elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
        MostActiveCompanyChange_List.append("Up By ")

for i in range(len(MostActiveCompanyNames_List)):
    MostActiveMarketValue_List[i] = MostActiveCompanyChange_List[i] + MostActiveMarketValue_List[i]


print(len(MostActiveMarketValue_List))
print(len(MostActiveCompanyChange_List))

MostActive_DataFrame = pd.DataFrame({"Most Active Company Names": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValue_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))



