import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

def FamousCompanies():
    URL = f"https://www.google.com/finance/"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL} : {e}")

    soup = BeautifulSoup(response.text, "lxml")

    FamousCompanyNames = soup.find_all("div", class_ = "ZvmM7")
    FamousMarketValues = soup.find_all("div", class_ = "YMlKec")
    FamousPercentages = soup.find_all("div", class_ = "JwB6zf")
    FamousChangeValues = soup.find_all("path")
    FamousCompanyCodes = soup.find_all("div", class_ = "COaKTb")

    FamousCompanyNames_List = []
    FamousChangeValues_List = []
    FamousMarketValues_List = []
    FamousPercentages_List = []
    FamousCompanyCodes_List = []

    for name in FamousCompanyNames:
        FamousCompanyNames_List.append(name.text)

    for colour in FamousChangeValues:
        if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
            FamousChangeValues_List.append("Down By ")
        elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
            FamousChangeValues_List.append("Up By ")

    for money in FamousMarketValues[10: 10 + len(FamousCompanyNames_List)]:
        FamousMarketValues_List.append(money.text)

    for percentage in FamousPercentages[10: 10 + len(FamousCompanyNames_List)]:
        FamousPercentages_List.append(percentage.text)

    for codename in FamousCompanyCodes:
        FamousCompanyCodes_List.append(codename.text)

    FamousCompanyCodes_List = FamousCompanyCodes_List[:6]

    FamousChangeValues_List = FamousChangeValues_List[10: 10 + len(FamousCompanyNames_List)]

    for i in range(len(FamousCompanyNames_List)):
        FamousPercentages_List[i] = FamousChangeValues_List[i] + FamousPercentages_List[i]

    Famous_Dataframe = pd.DataFrame({"Comapny Code": FamousCompanyCodes_List,"Company Name": FamousCompanyNames_List, "Market Value": FamousMarketValues_List, "Change Percentage": FamousPercentages_List})

    print("You maybe interested in...")
    print()
    print(Famous_Dataframe)
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