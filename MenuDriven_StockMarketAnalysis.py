# Importing necessary libraries and functions
from MostFollowedOnGoogle_StockMarketAnalysis import MostFollowedOnGoogle
from Gainers_StockMarketAnalysis import Gainers
from Losers_StockMarketAnalysis import Losers
from MostActive_StockMarketAnalysis import MostActive
from FamousCompanies_StockMarketAnalysis import FamousCompanies
from IndividualComapnyAnalysis_StockMarketAnalysis import IndividualCompanyAnalysis

# Function to display a header with a given title
def DisplayHeader(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

# Function to display the main menu options
def DisplayMenu():
    print("1. GAINERS")
    print("2. LOSERS")
    print("3. MOST ACTIVE")
    print("4. FAMOUS COMPANIES ON GOOGLE\n")

# Function to handle individual company analysis upon user request
def IndividualAnalysis_Imported():
    while True:
        user_input = input("Do you want to look into any company's stock details? (y/n): ").strip().lower()
        if user_input == 'y':
            IndividualCompanyAnalysis()
        elif user_input == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Main function to execute the program
def main():
    # Displaying the main header for the program
    DisplayHeader("STOCK ANALYSIS WITH GOOGLE FINANCE")

    # Displaying information about the most followed companies on Google
    DisplayHeader("MOST FOLLOWED COMPANIES ON GOOGLE")
    MostFollowedOnGoogle()
    IndividualAnalysis_Imported()  # Offering user option to explore individual companies
    print()

    # Displaying the main menu options
    DisplayHeader("MENU")
    DisplayMenu()

    try:
        option = int(input("Enter your option (1-4): "))  # Prompting user for menu option
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return

    # Processing user choice based on menu option
    if option == 1:
        DisplayHeader("GAINERS")
        Gainers_Dataframe = Gainers()  # Fetching and displaying gainer companies
        print(Gainers_Dataframe)
        IndividualAnalysis_Imported()  # Offering user option to explore individual companies

    elif option == 2:
        DisplayHeader("LOSERS")
        Losers_Dataframe = Losers()  # Fetching and displaying loser companies
        print(Losers_Dataframe)
        IndividualAnalysis_Imported()  # Offering user option to explore individual companies

    elif option == 3:
        DisplayHeader("MOST ACTIVE")
        MostActive_Dataframe = MostActive()  # Fetching and displaying most active companies
        print(MostActive_Dataframe)
        IndividualAnalysis_Imported()  # Offering user option to explore individual companies

    elif option == 4:
        DisplayHeader("FAMOUS COMPANIES ON GOOGLE")
        FamousCompanies_Dataframe = FamousCompanies()  # Fetching and displaying famous companies
        print(FamousCompanies_Dataframe)
        IndividualAnalysis_Imported()  # Offering user option to explore individual companies

    else:
        print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()  # Running the main function if this script is executed directly
