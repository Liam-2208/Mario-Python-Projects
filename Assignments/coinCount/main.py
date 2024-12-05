import os
from pymenu import select_menu
from typing import Union
from pathlib import Path
import re
import time
import json
from collections import OrderedDict
import keyboard

root_dir: Path = Path(os.getcwd())
data_file_path: Union[str, Path] = Path(root_dir / "data.txt" )
json_file_path: Union[str, Path] = Path(root_dir / "coin_data.json" )

with open(json_file_path, "r", encoding="utf-8") as f:
    try:
        coin_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding coin data: {e}")
        coin_data = {}

def load_data() -> dict[dict]:
    with open(data_file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding data: {e}")
            return {}
    return data

def save_data(data, path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        try:
            json.dump(data, f, indent=4)
        except (FileExistsError, FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error saving file: {e}")

def update_data(volunteer_name: str, coin: str, data: dict, correct_weight: bool) -> dict:
    correct: int = 1 if correct_weight else 0

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
        data[volunteer_name]["coins_checked"].append(coin)
        data[volunteer_name]["bags_checked"] += 1
        data[volunteer_name]["bags_correct"] += correct
        data[volunteer_name]["accuracy"] = (data[volunteer_name]["bags_correct"] / data[volunteer_name]["bags_checked"]) * 100

    if correct_weight:
        data[volunteer_name]["coins_correct"].append(coin)
    else:
        data[volunteer_name]["coins_incorrect"].append(coin)

    sorted_data = OrderedDict(
        sorted(data.items(), key=lambda x: x[1]["accuracy"], reverse=True)
    )

    save_data(sorted_data, data_file_path)
    return sorted_data
        

def check_bag(data: dict) -> dict[dict]:
    #  Get volunteers name
    volunteer_name: str = input("Enter volunteers name: ")
    while not re.search("^[a-zA-Z]+$", volunteer_name):
        print("Volunteer name can only contain letters.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        volunteer_name: str = input("Enter volunteers name: ")

    #  Get coin choice
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

    if coin_data[coin]["correct"]:
        print(f"{coin} is already correct.")
        time.sleep(2)
        main()

    bag_weight: float = 0
    while bag_weight <= 0:
        try:
            bag_weight = float(input("Enter bag weight (in g): "))
        except ValueError:
            print("Bag weight must be a number.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    
    if bag_weight < coin_data[coin]["expected_bag_weight"]:
        weight_difference: float = coin_data[coin]["expected_bag_weight"] - bag_weight
        coin_difference: float = round(weight_difference / coin_data[coin]["coin_weight"]) 
        print(f"Bag weight is too low. You are {coin_difference} {'coins' if coin_difference != 1 else 'coin'} short.")
        update_data(volunteer_name, coin, data, False) 
    elif bag_weight > coin_data[coin]["expected_bag_weight"]:
        weight_difference: float = bag_weight - coin_data[coin]["expected_bag_weight"]
        coin_difference: float = round(weight_difference / coin_data[coin]["coin_weight"]) 
        print(f"Bag weight is too high. You are {coin_difference} {'coins' if coin_difference != 1 else 'coin'} over.")
        update_data(volunteer_name, coin, data, False)
    else:
        print(f"Bag weight is within the expected range for {coin}.")
        coin_data[coin]["correct"] = True
        save_data(coin_data, json_file_path) 
        data = update_data(volunteer_name, coin, data, True)
    
def view_total(data) -> None:
    total_value: int = sum(coin_data[key]["bag_value"] for key in coin_data if coin_data[key]["correct"])
    total_bags_checked = sum(volunteer["bags_checked"] for volunteer in data.values())
    print(f"Total value of correct bags: £{total_value}")
    print(f"Total bags checked: {total_bags_checked}")
    print("Press Esc to go back.")
    
    while True:
        if keyboard.is_pressed("esc"):
            main()

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
            
def main() -> None:
    if not data_file_path.is_file():
        with open(data_file_path, "w") as f:
            f.write("{}") 

            print("Data file created.")
            os.system('cls' if os.name == 'nt' else 'clear')
    data = load_data()

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

    while True:
        if selected_option == options[0]:
            check_bag(data)
        elif selected_option == options[1]:
            view_total(data)
        elif selected_option == options[2]:
            list_volunteers(data)
        elif selected_option == options[3]:
            save_data(data, data_file_path)
            save_data(coin_data, json_file_path)
            print("Data saved successfully.")
            os.system('cls' if os.name == 'nt' else 'clear')
            exit(0)

if __name__ == "__main__":
    main()