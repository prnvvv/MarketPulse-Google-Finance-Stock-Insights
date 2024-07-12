import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup

def FamousCompanies():
    URL = f"https://www.google.com/finance/"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL} : {e}")

    soup = BeautifulSoup(response.text, "lxml")

    # Extracting data from specific classes in the HTML
    FamousCompanyNames = soup.find_all("div", class_ = "ZvmM7")
    FamousMarketValues = soup.find_all("div", class_ = "YMlKec")
    FamousPercentages = soup.find_all("div", class_ = "JwB6zf")
    FamousChangeValues = soup.find_all("path")
    FamousCompanyCodes = soup.find_all("div", class_ = "COaKTb")

    # Lists to store extracted data
    FamousCompanyNames_List = []
    FamousChangeValues_List = []
    FamousMarketValues_List = []
    FamousPercentages_List = []
    FamousCompanyCodes_List = []

    # Extracting company names
    for name in FamousCompanyNames:
        FamousCompanyNames_List.append(name.text)

    # Determining change values (up or down)
    for colour in FamousChangeValues:
        if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
            FamousChangeValues_List.append("Down By ")
        elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
            FamousChangeValues_List.append("Up By ")

    # Extracting market values
    for money in FamousMarketValues[10: 10 + len(FamousCompanyNames_List)]:
        FamousMarketValues_List.append(money.text)

    # Extracting percentage change
    for percentage in FamousPercentages[10: 10 + len(FamousCompanyNames_List)]:
        FamousPercentages_List.append(percentage.text)

    # Extracting company codes
    for codename in FamousCompanyCodes:
        FamousCompanyCodes_List.append(codename.text)

    # Trimming lists to desired lengths
    FamousCompanyCodes_List = FamousCompanyCodes_List[:6]
    FamousChangeValues_List = FamousChangeValues_List[10: 10 + len(FamousCompanyNames_List)]

    # Combining change values and percentages
    for i in range(len(FamousCompanyNames_List)):
        FamousPercentages_List[i] = FamousChangeValues_List[i] + FamousPercentages_List[i]

    # Creating a DataFrame with extracted data
    Famous_Dataframe = pd.DataFrame({"Company Code": FamousCompanyCodes_List, "Company Name": FamousCompanyNames_List, "Market Value": FamousMarketValues_List, "Change Percentage": FamousPercentages_List})

    # Printing the DataFrame
    print("You may be interested in...")
    print()
    print(Famous_Dataframe)
    print()

# Calling the function to execute
FamousCompanies()
