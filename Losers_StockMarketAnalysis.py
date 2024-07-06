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
LoserMarketValues = soup.find_all("div", class_ = "YMlKec")
LoserPercentages = soup.find_all("div", class_ = "JwB6zf")
LoserCompanyCodes = soup.find_all("div", class_ = "COaKTb")

LoserCompanyNames_List = []
LoserMarketValues_List = []
LoserPercentages_List = []
LoserCompanyCodes_List = []


for name in LoserCompanyNames:
    LoserCompanyNames_List.append(name.text)

for money in LoserMarketValues[10: 10+len(LoserCompanyNames_List)]:
    LoserMarketValues_List.append(money.text)

for percentage in LoserPercentages[10: 10+len(LoserCompanyNames_List)]:
    LoserPercentages_List.append(percentage.text)

for codename in LoserCompanyCodes:
    LoserCompanyCodes_List.append(codename.text)

LoserCompanyCodes_List = LoserCompanyCodes_List[:50]

GainerCompanyCodes_List = LoserCompanyCodes_List[:50]

for i in range(len(LoserCompanyNames_List)):
    LoserPercentages_List[i] = f"Down by {LoserPercentages_List[i]}"

Losers_DataFrame = pd.DataFrame({"Company Code": LoserCompanyCodes_List, "Company Name": LoserCompanyNames_List, "Market Value": LoserMarketValues_List, "Change Percentage": LoserPercentages_List}, index = np.arange(1, len(LoserCompanyNames_List)+1))

print()
print("LOSERS")
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

