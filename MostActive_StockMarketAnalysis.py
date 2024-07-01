import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/finance/markets/most-active"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}: {e}")
    exit()

soup = BeautifulSoup(response.text, "lxml")

# Adjust these class names based on actual website structure
MostActiveCompanyNames = soup.find_all("div", class_="ZvmM7")
MostActiveMarketValue = soup.find_all("div", class_="YMlKec")
MostActivePercentage = soup.find_all("div", class_="WlRRw IsqQVc fw-price-dn")

MostActiveCompanyNames_List = []
MostActiveMarketValue_List = []
MostActivePercentage_List = []

for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValue[10: 10+len(MostActiveCompanyNames_List)]:
    MostActiveMarketValue_List.append(money.text)

for perc in MostActivePercentage:
    MostActivePercentage_List.append(perc.text)

# Ensure all lists are of the same length
length = min(len(MostActiveCompanyNames_List), len(MostActiveMarketValue_List), len(MostActivePercentage_List))

MostActiveCompanyNames_List = MostActiveCompanyNames_List[:length]
MostActiveMarketValue_List = MostActiveMarketValue_List[:length]
MostActivePercentage_List = MostActivePercentage_List[:length]

MostActive_DataFrame = pd.DataFrame({
    "Most Active Company Names": MostActiveCompanyNames_List,
    "Market Value": MostActiveMarketValue_List,
    "Percentage Change": MostActivePercentage_List
}, index=np.arange(1, length + 1))

print(MostActive_DataFrame)
