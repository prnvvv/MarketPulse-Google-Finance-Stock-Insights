from MostFollowedOnGoogle_StockMarketAnalysis import MostFollowedOnGoogle
from Gainers_StockMarketAnalysis import Gainers
from Losers_StockMarketAnalysis import Losers
from MostActive_StockMarketAnalysis import MostActive
from FamousCompanies_StockMarketAnalysis import FamousCompanies
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

def main():
    print("\nSTOCK ANALYSIS WITH GOOGLE FINANCE\n")

    print("\nMOST FOLLOWED COMPANIES ON GOOGLE\n")
    MostFollowedOnGoogle()
    print()
    while True:
        user_input = input("Do you want to look into any company's stock details? (y/n): ")
        if user_input.lower() == 'y':
            IndividualCompanyAnalysis()
        elif user_input.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    print()

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
        Gainers_Dataframe = Gainers()
        print(Gainers_Dataframe)
        while True:
            user_input = input("Do you want to look into any company's stock details? (y/n): ")
            if user_input.lower() == 'y':
                IndividualCompanyAnalysis()
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    elif option == 2:
        print("\nLOSERS\n")
        Losers_Dataframe = Losers()
        print(Losers_Dataframe)
        while True:
            user_input = input("Do you want to look into any company's stock details? (y/n): ")
            if user_input.lower() == 'y':
                IndividualCompanyAnalysis()
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    elif option == 3:
        print("\nMOST ACTIVE\n")
        MostActive_Dataframe = MostActive()
        print(MostActive_Dataframe)
        while True:
            user_input = input("Do you want to look into any company's stock details? (y/n): ")
            if user_input.lower() == 'y':
                IndividualCompanyAnalysis()
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    elif option == 4:
        print("\nFAMOUS COMPANIES ON GOOGLE\n")
        FamousCompanies_Dataframe = FamousCompanies()
        print(FamousCompanies_Dataframe)
        while True:
            user_input = input("Do you want to look into any company's stock details? (y/n): ")
            if user_input.lower() == 'y':
                IndividualCompanyAnalysis()
            elif user_input.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    else:
        print("Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
