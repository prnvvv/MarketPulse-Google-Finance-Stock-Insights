from MostFollowedOnGoogle_StockMarketAnalysis import MostFollowedOnGoogle
from Gainers_StockMarketAnalysis import Gainers
from Losers_StockMarketAnalysis import Losers
from MostActive_StockMarketAnalysis import MostActive
from FamousCompanies_StockMarketAnalysis import FamousCompanies

print()
print("STOCK ANALYSIS WITH GOOGLE FINANCE")
print()

print()
print("MOST FOLLOWED COMPANIES ON GOOGLE")
print()
MostFollowedOnGoogle()
print()

print()
print("MENU")
print()
print("1. GAINERS")
print("2. LOSERS")
print("3. MOST ACTIVE")
print("4. FAMOUS COMPANIES ON GOOGLE")
print()

option = int(input("Enter your option: "))

if option == 1:
    print()
    print("GAINERS")
    print()
    Gainers_Dataframe = Gainers()
    print(Gainers_Dataframe)

