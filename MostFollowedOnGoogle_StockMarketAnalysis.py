import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def MostFollowedOnGoogle():
    # URL for fetching most followed companies data
    URL = f"https://www.google.com/finance/"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL} : {e}")

    soup = BeautifulSoup(response.text, "lxml")

    # Extracting data from specific classes in the HTML
    MFGCompanyNames = soup.find_all("div", class_ = "TwnKPb")
    MFGPercentages = soup.find_all("div", class_ = "JwB6zf")
    MFGChangeValues = soup.find_all("path")
    MFGCompanyCodes = soup.find_all("div", class_ = "COaKTb")

    # Lists to store extracted data
    MFGCompanyNames_List = []
    MFGPercentages_List = []
    MFGChangeValues_List = []
    MFGCompanyCodes_List = []

    # Extracting most followed company names
    for name in MFGCompanyNames:
        MFGCompanyNames_List.append(name.text)

    # Extracting most followed percentage changes and handling directional changes
    for colour in MFGChangeValues:
        if colour["d"] ==  "M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z":
            MFGChangeValues_List.append("Down By ")
        elif colour["d"] == "M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z":
            MFGChangeValues_List.append("Up By ")

    # Trimming and formatting percentage change list
    MFGChangeValues_List = MFGChangeValues_List[16: 16 + len(MFGCompanyNames_List)]
    for i in range(len(MFGCompanyNames_List)):
        MFGPercentages_List.append(MFGChangeValues_List[i] + MFGPercentages[16 + i].text)

    # Extracting most followed company codes
    for codename in MFGCompanyCodes:
        MFGCompanyCodes_List.append(codename.text)

    # Trimming company codes list to desired length
    MFGCompanyCodes_List = MFGCompanyCodes_List[6: 12]

    # Creating a DataFrame with extracted data
    MFG_Dataframe = pd.DataFrame({"Company Code": MFGCompanyCodes_List, "Company Name": MFGCompanyNames_List, "Change Percentage": MFGPercentages_List})

    # Printing the DataFrame
    print()
    print("MOST FOLLOWED ON GOOGLE")
    print()
    
    return MFG_Dataframe

