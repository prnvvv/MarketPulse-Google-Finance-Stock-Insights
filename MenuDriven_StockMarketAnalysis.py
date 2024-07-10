from MostFollowedOnGoogle_StockMarketAnalysis import MostFollowedOnGoogle
from Gainers_StockMarketAnalysis import Gainers
from Losers_StockMarketAnalysis import Losers
from MostActive_StockMarketAnalysis import MostActive
from FamousCompanies_StockMarketAnalysis import FamousCompanies
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

def main():
    print("\nSTOCK ANALYSIS WITH GOOGLE FINANCE\n")

    # Display most followed companies on Google
    print("\nMOST FOLLOWED COMPANIES ON GOOGLE\n")
    MostFollowedOnGoogle()
    print()

    # Perform individual company analysis
    IndividualCompanyAnalysis()
    print()

    # Display the menu
    print("\nMENU\n")
    print("1. GAINERS")
    print("2. LOSERS")
    print("3. MOST ACTIVE")
    print("4. FAMOUS COMPANIES ON GOOGLE\n")

    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    if option == 1:
        print("\nGAINERS\n")
        gainers_df = Gainers()
        print(gainers_df)
        IndividualCompanyAnalysis()

    elif option == 2:
        print("\nLOSERS\n")
        losers_df = Losers()
        print(losers_df)
        IndividualCompanyAnalysis()

    elif option == 3:
        print("\nMOST ACTIVE\n")
        most_active_df = MostActive()
        print(most_active_df)
        IndividualCompanyAnalysis()

    elif option == 4:
        print("\nFAMOUS COMPANIES ON GOOGLE\n")
        famous_companies_df = FamousCompanies()
        print(famous_companies_df)
        IndividualCompanyAnalysis()

    else:
        print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
