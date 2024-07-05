import numpy as np
import pandas as pd
import requests 
from bs4 import BeautifulSoup

def IndividualCompanyAnalysis():
    code = input("Enter the Company code: ")

    URL = f"https://www.google.com/finance/quote/{code.upper()}:NSE"

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {URL} : {e}")

    soup = BeautifulSoup(response.text, "lxml")

    Companyname = soup.find("div", class_ = "zzDege").text
    CompanyMarketValue = soup.find("div", class_ = "YMlKec fxKbKc").text
    CompanyPercentage = soup.find_all("div", class_ = "JwB6zf")
    Date = soup.find("div", class_ = "ygUjEc").text

    CompanyPercentage_List = []

    for percentage in CompanyPercentage:
        CompanyPercentage_List.append(percentage.text)
    CompanyPercentage = CompanyPercentage_List[19]

    print()
    print(Date)
    print()

    print(pd.Series([Companyname, CompanyMarketValue, CompanyPercentage], index = ["Company Name", "Market Value", "Percentage"]))

IndividualCompanyAnalysis()