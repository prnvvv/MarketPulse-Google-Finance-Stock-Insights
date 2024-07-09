import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

def MostFollowedOnGoogle():
    
URL = f"https://www.google.com/finance/"

try:
    response = requests.get(URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {URL} : {e}")

soup = BeautifulSoup(response.text, "lxml")

MFGCompanyNames = soup.find_all("div", class_ = "TwnKPb")
MFGPercentages = soup.find_all("div", class_ = "JwB6zf")
MFGChangeValues = soup.find_all("path")
MFGCompanyCodes = soup.find_all("div", class_ = "COaKTb")

MFGCompanyNames_List = []
MFGPercentages_List = []
MFGChangeValues_List = []
MFGCompanyCodes_List = []

for name in MFGCompanyNames:
    MFGCompanyNames_List.append(name.text)

for percentage in MFGPercentages[16: 16 + len(MFGCompanyNames_List)]:
    MFGPercentages_List.append(percentage.text)

for codename in MFGCompanyCodes:
    MFGCompanyCodes_List.append(codename.text)

MFGCompanyCodes_List = MFGCompanyCodes_List[6: 12]

for colour in MFGChangeValues:
    if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
        MFGChangeValues_List.append("Down By ")
    elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
        MFGChangeValues_List.append("Up By ")

MFGChangeValues_List = MFGChangeValues_List[16: 16 + len(MFGCompanyNames_List)]

for i in range(len(MFGCompanyNames_List)):
    MFGPercentages_List[i] = MFGChangeValues_List[i] + MFGPercentages_List[i]

MFG_Dataframe = pd.DataFrame({"Company Code": MFGCompanyCodes_List, "Company Name": MFGCompanyNames_List, "Change Percentage": MFGPercentages_List})

print()
print("Most Followed on Google")
print()
print(MFG_Dataframe)
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