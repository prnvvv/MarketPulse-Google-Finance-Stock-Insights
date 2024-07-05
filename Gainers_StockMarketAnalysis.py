import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/markets/gainers"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL} : {e}")

soup = BeautifulSoup(response.text, "lxml")

GainerCompanyNames = soup.find_all("div", class_ = "ZvmM7")
GainerMarketValues = soup.find_all("div", class_ = "YMlKec")
GainerPercentages = soup.find_all("div", class_ = "JwB6zf")
GainerCompanyCode = soup.find_all("div", class_ = "COaKTb")

GainerCompanyNames_List = []
GainerMarketValues_List = []
GainerPercentages_List = []
GainerCompanyCode_List = []

for name in GainerCompanyNames:
    GainerCompanyNames_List.append(name.text)

for money in GainerMarketValues[10: 10+len(GainerCompanyNames_List)]:
    GainerMarketValues_List.append(money.text)

for percentage in GainerPercentages[10: 10+len(GainerCompanyNames_List)]:
    GainerPercentages_List.append(percentage.text)

for codename in GainerCompanyCode:
    GainerCompanyCode_List.append(codename.text)


Gainers_DataFrame = pd.DataFrame({"Gainer Company Names": GainerCompanyNames_List, "Market Value": GainerMarketValue_List, "Increase Percentage": GainerPercentages_List}, index = np.arange(1, len(GainerCompanyNames_List)+1))

#print(Gainers_DataFrame)

