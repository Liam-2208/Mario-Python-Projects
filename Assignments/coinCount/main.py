# Import necessary libraries
import os
from pymenu import select_menu
from typing import Union
from pathlib import Path
import re
import time
import json
from collections import OrderedDict
import keyboard
import requests

# Define file paths
root_dir: Path = Path(os.getcwd())
data_file_path: Union[str, Path] = Path(root_dir / "data.txt" )
json_file_path: Union[str, Path] = Path(root_dir / "coin_data.json" )

# Function to request coin data from GitHub
def request_coin_data() -> dict:
    url = "https://raw.githubusercontent.com/aem2231/python-projects/refs/heads/master/Assignments/coinCount/coin_data.json"
    try:
        coin_data = requests.get(url)
        coin_data.raise_for_status()  # Raise an exception for bad status codes
        return coin_data.json()  # Parse the response content as JSON and return it
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coin data: {e}")
        print("Please check your internet connection and try again.")
        time.sleep(1.5)
        return {}

# Function to get coin data from local file or GitHub
def get_coin_data() -> dict[dict[float, float, float, float, bool]]:
    try:
        # Try to open and read the local JSON file
        with open(json_file_path, "r", encoding="utf-8") as f:
            try:
                coin_data = json.load(f)
            except json.JSONDecodeError as e:
                # If there's an error decoding the JSON, fetch from GitHub
                print(f"Error decoding coin data: {e}\nFetching coin data from GitHub...")
                f.close()
                Path.unlink(json_file_path)  # Delete the file
                time.sleep(1.5)
                coin_data = request_coin_data()
                save_data(coin_data, json_file_path)
    except FileNotFoundError:
        # If the file is not found, fetch from GitHub
        print("Coin data file not found. Requesting data from GitHub...")
        for i in range(5):
            coin_data = request_coin_data()
            if coin_data != {}:
                break
        if coin_data == {}:
            print("Failed to fetch coin data from GitHub. Please try again later.")
            exit(0)
        save_data(coin_data, json_file_path)
    
    return coin_data  

# Function to save data to a file
def save_data(data: dict[dict], file_path: str) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving data to {file_path}: {e}")

# Function to load data from a file
def load_data() -> dict[dict]:
    with open(data_file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding data: {e}")
            data: dict[dict] = {}
    return data

# Function to update volunteer data
def update_data(volunteer_name: str, coin: str, data: dict, correct_weight: bool) -> dict:
    correct: int = 1 if correct_weight else 0
    volunteer_name = volunteer_name.strip().title()

    # If the volunteer is new, initialize their data
    if volunteer_name not in data:
        data[volunteer_name] = {
            "coins_checked": [coin],
            "coins_incorrect": [],
            "coins_correct": [],
            "bags_checked": 1,
            "bags_correct": correct,
            "accuracy": 0
        }
        data[volunteer_name]["accuracy"] = (data[volunteer_name]["bags_correct"] / data[volunteer_name]["bags_checked"]) * 100
    else:
        # Update existing volunteer's data
        data[volunteer_name]["coins_checked"].append(coin)
        data[volunteer_name]["bags_checked"] += 1
        data[volunteer_name]["bags_correct"] += correct
        data[volunteer_name]["accuracy"] = (data[volunteer_name]["bags_correct"] / data[volunteer_name]["bags_checked"]) * 100

    # Update correct or incorrect coins list
    if correct_weight:
        data[volunteer_name]["coins_correct"].append(coin)
    else:
        data[volunteer_name]["coins_incorrect"].append(coin)

    # Sort data by accuracy
    sorted_data = OrderedDict(
        sorted(data.items(), key=lambda x: x[1]["accuracy"], reverse=True)
    )

    # Save and return the updated data
    save_data(sorted_data, data_file_path)
    return sorted_data

# Function to check a bag of coins
def check_bag(data: dict) -> dict[dict]:
    # Get volunteer's name
    volunteer_name: str = input("Enter volunteers name: ")
    while not re.search("^[a-zA-Z]+$", volunteer_name):
        print("Volunteer name can only contain letters.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        volunteer_name: str = input("Enter volunteers name: ")

    # Get coin choice
    coin_options: list[str] = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
    coin_index: int = -1
    while coin_index < 0 or coin_index >= len(coin_options):
        try:
            coin = select_menu.create_select_menu(coin_options, "Pick an coin: ")
            coin_index = coin_options.index(coin)
        except (IndexError, ValueError) as e:
            print(f"Invalid option: {e}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    coin: str = coin_options[coin_index]

    # Check if the coin is already correct
    if coin_data[coin]["correct"]:
        print(f"{coin} has already been weighed and is correct.")
        time.sleep(2)
        main()

    # Get bag weight
    bag_weight: float = 0
    while bag_weight <= 0:
        try:
            bag_weight = float(input("Enter bag weight (in g): "))
        except ValueError:
            print("Bag weight must be a number.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    
    # Check if the bag weight is correct
    if bag_weight != coin_data[coin]["expected_bag_weight"]:
        weight_difference: float = coin_data[coin]["expected_bag_weight"] - bag_weight
        coin_difference: float = round(weight_difference / coin_data[coin]["coin_weight"], 0) 
        print(f"Bag weight is too low. You are {abs(coin_difference)} {'coins' if coin_difference != 1 else 'coin'} {'short' if bag_weight < coin_data[coin]['expected_bag_weight'] else 'over'}.")
        update_data(volunteer_name, coin, data, False)
        time.sleep(2)
        main()
    else:
        print(f"Bag weight is within the expected range for {coin}.")
        coin_data[coin]["correct"] = True
        save_data(coin_data, json_file_path) 
        data = update_data(volunteer_name, coin, data, True)
        time.sleep(2)
        main()

# Function to view total value and bags checked
def view_total(data) -> None:
    total_value: int = sum(coin_data[key]["bag_value"] for key in coin_data if coin_data[key]["correct"])
    total_bags_checked = sum(volunteer["bags_checked"] for volunteer in data.values())
    total_bags_checked_correct = sum(volunteer["bags_correct"] for volunteer in data.values())


    print(f"Total value of correct bags: £{total_value}")
    print(f"Total correct bags: {total_bags_checked_correct}")
    print(f"Total incorrect: {total_bags_checked - total_bags_checked_correct}")
    print(f"Total bags checked: {total_bags_checked}")
    print(f"Average accuracy: {sum(volunteer['accuracy'] for volunteer in data.values()) / len(data)}%")
    print("Press Esc to go back.")
    
    while True:
        if keyboard.is_pressed("esc"):
            main()

# Function to list volunteers and their stats
def list_volunteers(data) -> None:
    volunters: list[str] = list(data.keys()) + ["All", "Main Menu"]
    choice: str = ""

    if len(volunters) == 2:
        print("No volunteers found.")
        time.sleep(2)
        main()

    while True:
        try:
            choice: str = select_menu.create_select_menu(volunters, "Volunteers sorted by accuracy.\nSelect a volunteer or 'all' for more information: ")
        except (IndexError, ValueError) as e:
            print(f"Invalid option: {e}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        if choice == "All":
            # Display all volunteers' data
            for volunteer, details in data.items():
                print(f"Volunteer: {volunteer}")
                print(f"  Coins Checked: {', '.join(details['coins_checked'])}")
                print(f"  Bags Checked: {details['bags_checked']}")
                print(f"  Bags Correct: {details['bags_correct']}")
                print(f"  Accuracy: {details['accuracy']}%")
                print("-" * 40)
            print("\nPress Esc to go back.")

            while True:            
                if keyboard.is_pressed("esc"):
                    return None
                
        elif choice == "Main Menu":
            main()
        else:
            # Display individual volunteer's data
            print(f"Volunteer: {choice}")
            print(f"  Coins Checked: {', '.join(data[choice]['coins_checked'])}")
            print(f"  Bags Checked: {data[choice]['bags_checked']}")
            print(f"  Bags Correct: {data[choice]['bags_correct']}")
            print(f"  Accuracy: {data[choice]['accuracy']}%")
            print("-" * 40)
            print("\nPress Esc to go back.")

            while True:            
                if keyboard.is_pressed("esc"):
                    return None

# Main function to run the program
def main() -> None:
    global coin_data
    coin_data = get_coin_data()

    # Create data file if it doesn't exist
    if not data_file_path.is_file():
        with open(data_file_path, "w") as f:
            f.write("{}") 

            print("Data file created.")
            os.system('cls' if os.name == 'nt' else 'clear')
    data = load_data()

    # Main menu loop
    options: list[str] = ["Check Bag", "View Total", "List Volunteers", "Save and Quit"]
    selected_option: str = ""
    while selected_option not in options:
        try:
            print("Press 'tab' at any time to quit.")
            selected_option: str = select_menu.create_select_menu(options, "Pick an option: ")
        except (IndexError, ValueError) as e:
            print(f"Invalid option: {e}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

    # Execute the selected option
    while True:
        if selected_option == options[0]:
            check_bag(data)
        elif selected_option == options[1]:
            view_total(data)
        elif selected_option == options[2]:
            list_volunteers(data)
        elif selected_option == options[3]:
            save_data(data, data_file_path)
            print("Data saved successfully.")
            os.system('cls' if os.name == 'nt' else 'clear')
            exit(0)

if __name__ == "__main__":
    main()
