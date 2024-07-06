import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

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
GainerCompanyCodes = soup.find_all("div", class_ = "COaKTb")

GainerCompanyNames_List = []
GainerMarketValues_List = []
GainerPercentages_List = []
GainerCompanyCodes_List = []

for name in GainerCompanyNames:
    GainerCompanyNames_List.append(name.text)

for money in GainerMarketValues[10: 10+len(GainerCompanyNames_List)]:
    GainerMarketValues_List.append(money.text)

for percentage in GainerPercentages[10: 10+len(GainerCompanyNames_List)]:
    GainerPercentages_List.append(percentage.text)

for codename in GainerCompanyCodes:
    GainerCompanyCodes_List.append(codename.text)

GainerCompanyCodes_List = GainerCompanyCodes_List[:50]

for i in range(len(GainerCompanyNames_List)):
    GainerPercentages_List[i] = f"Up by {GainerPercentages_List[i]}"


Gainers_DataFrame = pd.DataFrame({"Company Code": GainerCompanyCodes_List, "Company Name": GainerCompanyNames_List, "Market Value": GainerMarketValues_List, "Change Percentage": GainerPercentages_List}, index = np.arange(1, len(GainerCompanyNames_List)+1))

print()
print(Gainers_DataFrame)
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