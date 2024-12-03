import pandas as pd
from pymenu import select_menu
import time
import os
import matplotlib.pyplot as plt


# Outputs the initial menu and checks validates the input
def main_menu():
    options: list[str] = ["Total income by source", "Income Sources By Day"]
    choice: str = ""

    while choice not in options:
        try:
            choice: str = select_menu.create_select_menu(options, "Recoats Adventure Park\nSelect an option: ")
        except (IndexError, TypeError, ValueError) as e:
            print(f"Invalid option: {e}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    return options.index(choice)

# Submenu for totals, provides type check validation for the input
def total_menu ():
    options: list[str] = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]
    choice: str = ""
    
    while choice not in options:
        try:
            choice: str = select_menu.create_select_menu(options, "Total Income By Source\nSelect an option:")
        except (IndexError, TypeError, ValueError) as e:
            print(f"Invlaid options: {e}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

def income_sources_by_day(source: str) -> None:
    sorted_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    df = pd.read_csv('Task4a_data.csv')
    income_sources_by_day = df.groupby("Day")[source].sum()
    income_sources_by_day.index = pd.Categorical(income_sources_by_day.index, categories=sorted_weekdays, ordered=True)
    income_sources_by_day = income_sources_by_day.sort_index()
    days = sorted_weekdays
    income = income_sources_by_day.values.tolist()

    plt.figure(figsize=(10, 6))
    plt.bar(days, income)
    plt.title(f"Income from {source} by Day")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# takes the total submenu input and converts the number to a string of the source name
def convert_total_menu_choice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "Tickets"
    elif total_menu_choice == "2":
        total_choice = "Gift Shop"
    elif total_menu_choice == "3":
        total_choice= "Snack Stand"
    else:
        total_choice = "Pictures"  
    
    return total_choice

# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg

main_menu_choice = main_menu()
if main_menu_choice == 0:
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_choice(total_menu_choice)
    print(get_total_data(total_choice))
elif main_menu_choice == 1:
    options: list[str] = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]
    source = ""
    while source not in options:
        try:
            source = select_menu.create_select_menu(options, "Select an income source:")
        except (IndexError, TypeError, ValueError) as e:
            print(f"Invalid option: {e}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            
    income_sources_by_day(source)
