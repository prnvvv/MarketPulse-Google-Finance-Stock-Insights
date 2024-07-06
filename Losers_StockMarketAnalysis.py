import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

URL = f"https://www.google.com/finance/markets/losers"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL}: {e}")

soup = BeautifulSoup(response.text, "lxml")

LoserCompanyNames = soup.find_all("div", class_ = "ZvmM7")
LoserMarketValue = soup.find_all("div", class_ = "YMlKec")
LoserPercentage = soup.find_all("div", class_ = "JwB6zf")

LoserCompanyNames_List = []
LoserMarketValue_List = []
LoserPercentage_List = []

for name in LoserCompanyNames:
    LoserCompanyNames_List.append(name.text)

for money in LoserMarketValue[10: 10+len(LoserCompanyNames_List)]:
    LoserMarketValue_List.append(money.text)

for percentage in LoserPercentage[10: 10+len(LoserCompanyNames_List)]:
    LoserPercentage_List.append(percentage.text)

Losers_DataFrame = pd.DataFrame({"Gainer Company Names": LoserCompanyNames_List, "Market Value": LoserMarketValue_List, "Increase Percentage": LoserPercentage_List}, index = np.arange(1, len(LoserCompanyNames_List)+1))

print()
print(Losers_DataFrame)
print()

while True:
    CompanyDetails = input("Do you want to look into any Company's stock details? (y/n): ")

    if CompanyDetails.lower() == 'y' or CompanyDetails.lower() == 'yes':
        IndividualCompanyAnalysis()
    elif CompanyDetails.lower() == 'n' or CompanyDetails.lower() == 'no':
        print()
        break
    else:
        print()
        print("Invalid Input")
        print()

