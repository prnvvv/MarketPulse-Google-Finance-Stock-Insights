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
MostActiveCompanyAbbr = soup.find_all("div", class_ = "COaKTb")

MostActiveCompanyNames_List = []
MostActiveMarketValue_List = []
MostActivePercentage_List = []
MostActiveChangeValue_List = []
MostActiveCompanyAbbr_List = []

for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValue[10: 10+len(MostActiveCompanyNames_List)]:
    MostActiveMarketValue_List.append(money.text)

for abbrnName in MostActiveCompanyAbbr[:len(MostActiveCompanyNames_List)]:
    MostActiveCompanyAbbr_List.append(abbrnName.text)

MostActive_DataFrame = pd.DataFrame({"Most Active Company Names": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValue_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))

print(MostActive_DataFrame)

for i in MostActiveCompanyAbbr_List:
    print(i.upper())
    NextPageURL = f"https://www.google.com/finance/quote/{i.upper}:NSE"


