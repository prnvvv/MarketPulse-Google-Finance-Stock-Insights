import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = f"https://www.google.com/finance/markets/gainers"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}.")

soup = BeautifulSoup(response.text, "lxml")

GainerCompanyNames = soup.find_all("div", class_ = "ZvmM7")
GainerMarketValue = soup.find_all("div", class_ = "YMlKec")
GainerPercentage = soup.find_all("span", class_ = "V53LMb")

GainerCompanyNames_List = []
GainerMarketValue_List = []

for name in GainerCompanyNames:
    GainerCompanyNames_List.append(name.text)

for money in GainerMarketValue[10: 10+len(GainerCompanyNames_List)]:
    GainerMarketValue_List.append(money.text)

for percentage in GainerPercentage:
    print(percentage.text)


Gainers_DataFrame = pd.DataFrame({"Gainer Company Names": GainerCompanyNames_List, "Market Value": GainerMarketValue_List}, index = np.arange(1, len(GainerCompanyNames_List)+1))


