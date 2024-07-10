from MostFollowedOnGoogle_StockMarketAnalysis import MostFollowedOnGoogle
from Gainers_StockMarketAnalysis import Gainers
from Losers_StockMarketAnalysis import Losers
from MostActive_StockMarketAnalysis import MostActive
from FamousCompanies_StockMarketAnalysis import FamousCompanies
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

def DisplayHeader(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

def DisplayMenu():
    print("1. GAINERS")
    print("2. LOSERS")
    print("3. MOST ACTIVE")
    print("4. FAMOUS COMPANIES ON GOOGLE\n")

def IndividualAnalysis_Imported():
    while True:
        user_input = input("Do you want to look into any company's stock details? (y/n): ").strip().lower()
        if user_input == 'y':
            IndividualCompanyAnalysis()
        elif user_input == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    DisplayHeader("STOCK ANALYSIS WITH GOOGLE FINANCE")

    DisplayHeader("MOST FOLLOWED COMPANIES ON GOOGLE")
    MostFollowedOnGoogle()
    IndividualAnalysis_Imported()
    print()

    DisplayHeader("MENU")
    DisplayMenu()

    try:
        option = int(input("Enter your option (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    if option == 1:
        DisplayHeader("GAINERS")
        Gainers_Dataframe = Gainers()
        print(Gainers_Dataframe)
        IndividualAnalysis_Imported()

    elif option == 2:
        DisplayHeader("LOSERS")
        Losers_Dataframe = Losers()
        print(Losers_Dataframe)
        IndividualAnalysis_Imported()

    elif option == 3:
        DisplayHeader("MOST ACTIVE")
        MostActive_Dataframe = MostActive()
        print(MostActive_Dataframe)
        IndividualAnalysis_Imported()

    elif option == 4:
        DisplayHeader("FAMOUS COMPANIES ON GOOGLE")
        FamousCompanies_Dataframe = FamousCompanies()
        print(FamousCompanies_Dataframe)
        IndividualAnalysis_Imported()

    else:
        print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
