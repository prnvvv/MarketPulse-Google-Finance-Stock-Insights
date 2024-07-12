import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def Losers():
    URL = f"https://www.google.com/finance/markets/losers"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL}: {e}")

    soup = BeautifulSoup(response.text, "lxml")

    # Extracting data from specific classes in the HTML
    LoserCompanyNames = soup.find_all("div", class_ = "ZvmM7")
    LoserMarketValues = soup.find_all("div", class_ = "YMlKec")
    LoserPercentages = soup.find_all("div", class_ = "JwB6zf")
    LoserCompanyCodes = soup.find_all("div", class_ = "COaKTb")

    # Lists to store extracted data
    LoserCompanyNames_List = []
    LoserMarketValues_List = []
    LoserPercentages_List = []
    LoserCompanyCodes_List = []

    # Extracting loser company names
    for name in LoserCompanyNames:
        LoserCompanyNames_List.append(name.text)

    # Extracting loser market values
    for money in LoserMarketValues[10: 10+len(LoserCompanyNames_List)]:
        LoserMarketValues_List.append(money.text)

    # Extracting loser percentage changes
    for percentage in LoserPercentages[10: 10+len(LoserCompanyNames_List)]:
        LoserPercentages_List.append(percentage.text)

    # Extracting loser company codes
    for codename in LoserCompanyCodes:
        LoserCompanyCodes_List.append(codename.text)

    # Trimming loser company codes list to desired length
    LoserCompanyCodes_List = LoserCompanyCodes_List[:50]

    # Formatting percentage changes
    for i in range(len(LoserCompanyNames_List)):
        LoserPercentages_List[i] = f"Down by {LoserPercentages_List[i]}"

    # Creating a DataFrame with extracted data
    Losers_DataFrame = pd.DataFrame({"Company Code": LoserCompanyCodes_List, "Company Name": LoserCompanyNames_List, "Market Value": LoserMarketValues_List, "Change Percentage": LoserPercentages_List}, index = np.arange(1, len(LoserCompanyNames_List)+1))

    # Printing the DataFrame
    print()
    print("LOSERS")
    print()
    
    return Losers_DataFrame

