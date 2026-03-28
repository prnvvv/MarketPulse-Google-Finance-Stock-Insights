import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup

def IndividualCompanyAnalysis():
    print()
    code = input("Enter the Company code: ")

    # Constructing the URL based on user input
    URL = f"https://www.google.com/finance/quote/{code.upper()}:NSE"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL} : {e}")
        return None

    soup = BeautifulSoup(response.text, "lxml")

    # Extracting specific data from the HTML
    company_name_element = soup.find("div", class_ = "zzDege")
    Companyname = company_name_element.text if company_name_element else "N/A"
    
    company_value_element = soup.find("div", class_ = "YMlKec fxKbKc")
    CompanyMarketValue = company_value_element.text if company_value_element else "N/A"
    
    CompanyPercentage = soup.find_all("div", class_ = "JwB6zf")
    
    date_element = soup.find("div", class_ = "ygUjEc")
    Date = date_element.text if date_element else "N/A"

    # Extracting and formatting percentage change
    CompanyPercentage_List = []
    for percentage in CompanyPercentage:
        CompanyPercentage_List.append(percentage.text)
    CompanyPercentage = CompanyPercentage_List[19]

    IndividualCompanyAnalysis_Dataframe = pd.Series([Companyname, CompanyMarketValue, CompanyPercentage], index = ["Company Name", "Market Value", "Percentage"])
    # Printing the extracted information
    print()
    print(Date)
    print()
    
    return IndividualCompanyAnalysis_Dataframe
