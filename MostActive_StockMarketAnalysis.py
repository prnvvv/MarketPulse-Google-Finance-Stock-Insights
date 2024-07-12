import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def MostActive():
    # URL for fetching most active companies data
    URL = f"https://www.google.com/finance/markets/most-active"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL}.")

    soup = BeautifulSoup(response.text, "lxml")

    # Extracting data from specific classes in the HTML
    MostActiveCompanyNames = soup.find_all("div", class_ = "ZvmM7")
    MostActiveMarketValues = soup.find_all("div", class_ = "YMlKec")
    MostActiveCompanyChanges = soup.find_all("path")
    MostActivePercentages = soup.find_all("div", class_ = "JwB6zf")
    MostActiveCompanyCodes = soup.find_all("div", class_ = "COaKTb")

    # Lists to store extracted data
    MostActiveCompanyNames_List = []
    MostActiveMarketValues_List = []
    MostActivePercentages_List = []
    MostActiveCompanyChanges_List = []
    MostActiveCompanyCodes_List = []

    # Extracting most active company names
    for name in MostActiveCompanyNames:
        MostActiveCompanyNames_List.append(name.text)

    # Extracting most active market values
    for money in MostActiveMarketValues[10: 10 + len(MostActiveCompanyNames_List)]:
        MostActiveMarketValues_List.append(money.text)

    # Extracting most active percentage changes and handling directional changes
    for colour in MostActiveCompanyChanges:
        if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
            MostActiveCompanyChanges_List.append("Down By ")
        elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
            MostActiveCompanyChanges_List.append("Up By ")

    # Trimming and formatting percentage change list
    MostActiveCompanyChanges_List = MostActiveCompanyChanges_List[10: 10 + len(MostActiveCompanyNames_List)]
    for i in range(len(MostActiveCompanyNames_List)):
        MostActivePercentages_List[i] = MostActiveCompanyChanges_List[i] + MostActivePercentages_List[i]

    # Extracting most active company codes
    for codename in MostActiveCompanyCodes:
        MostActiveCompanyCodes_List.append(codename.text)

    # Trimming company codes list to desired length
    MostActiveCompanyCodes_List = MostActiveCompanyCodes_List[:50]

    # Creating a DataFrame with extracted data
    MostActive_DataFrame = pd.DataFrame({"Company Code": MostActiveCompanyCodes_List,"Company Name": MostActiveCompanyNames_List, "Market Value": MostActiveMarketValues_List, "Change Percentage": MostActivePercentages_List}, index = np.arange(1, len(MostActiveCompanyNames_List)+1))

    # Printing the DataFrame
    print()
    print("MOST ACTIVE COMPANIES")
    print()
    
    return MostActive_DataFrame
    
