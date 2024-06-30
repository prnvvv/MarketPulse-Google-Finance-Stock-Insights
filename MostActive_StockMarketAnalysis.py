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
MostActivePercentage = soup.find_all("span")

MostActiveCompanyNames_List = []
MostActiveMarketValue_List = []
MostActivePercentage_List = []

for name in MostActiveCompanyNames:
    MostActiveCompanyNames_List.append(name.text)

for money in MostActiveMarketValue[10: 10+len(MostActiveCompanyNames_List)]:
    MostActiveMarketValue_List.append(money.text)

for percentage in MostActivePercentage:
    if percentage.class_ == "NydbP VOXKNe":
        print("y")

#MostActive_DataFrame = pd.DataFrame({"Gainer Company Names": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValue_List, "Increase Percentage": MostActivePercentage_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))


