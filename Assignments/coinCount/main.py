import os
import math
from pymenu import select_menu
from typing import Union
from pathlib import Path
import re
import time
import json

root_dir: Path = Path(os.getcwd())
data_file_path: Union[str, Path] = Path(root_dir / "data.txt")

bag_data: dict[str: list[str, float]] = {
    #Coin  amount  coin weight
    "£2": ["£20", 12.00],
    "£1": ["£20", 8.75],
    "50p": ["£10", 8.00],
    "20p": ["£10", 5.00],
    "10p": ["£5", 6.50],
    "5p": ["£5", 2.35],
    "2p": ["£1", 7.12],
    "1p": ["£1", 3.56]
}

coin_data: dict[str: float] = {
    #Coin  value
    "£20": 20.0,
    "£10": 10.0,
    "£5": 5.0,
    "£2": 2.0,
    "£1": 1.0,
    "50p": 0.5,
    "20p": 0.2,
    "10p": 0.1,
    "5p": 0.05,
    "2p": 0.02,
    "1p": 0.01
}

def load_data() -> list[dict]:
    with open(data_file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding data: {e}")
    return data

def save_data(data) -> None:
    with open(data_file_path, "w", encoding="utf-8") as f:
        try:
            f.write(data)
        except (FileExistsError, FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error saving file: {e}")

def check_bag() -> bool:
    data: dict[str: list] = {}
    volunteer_name: str = input("Enter volunteers name: ")
    while not re.search("^[a-zA-Z]+$", volunteer_name):
        print("Volunteer name can only contain letters.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        volunteer_name: str = input("Enter volunteers name: ")

    coin_options: list[str] = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
    coin: int = select_menu.create_select_menu(coin_options, "Pick an coin: ")

    #coin_index: str = coin_options.index(selected_coin_option) # Gets the coin name as a string, eg: '£2
    coin_value: float = coin_data[coin] # Gets the value of the coin, eg 2.0 or 0.5
    coin_weight: float = bag_data[coin][1] # Gets the coins weight, eg 12.00
    expected_value: float = coin_data[bag_data[coin][0]]
    expected_weight: float = expected_value / coin_weight
    expected_coin_quantity: int = expected_value / coin_value

    try:
        weight: float = float(input("Enter weight "))
        coin_quantity: int = round(weight / coin_weight)
        while weight != expected_weight:
            coin_offset: int = expected_coin_quantity - coin_quantity
            print(f"Incorrect weight!\n")
            if coin_offset > 0:
                print(f"Add ≈{coin_offset} more coins.")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif coin_offset < 0:
                print(f"Remove ≈{abs(coin_offset)} to continue.")
            weight: float = float(input("Enter weight "))

    except (TypeError, ValueError) as e:
        print(f"Value must be of type int: {e}")

def view_total() -> None:
    pass

def list_volunteers() -> None:
    pass

def main() -> None:
    # Check if data file exists
    if not data_file_path.is_file():
        with open(data_file_path, "w"):
            print("Data file created.")
            os.system('cls' if os.name == 'nt' else 'clear')

    data = load_data()
    print(data)
    time.sleep(3)


    options: list[str] = ["Check Bag", "View Total", "List Volunteers", "Save and Quit"]
    selected_option: str = select_menu.create_select_menu(options, "Pick an option: ")

    if selected_option == options[0]:
        check_bag()
    elif selected_option == options[1]:
        view_total()
    elif selected_option == options[2]:
        list_volunteers()

main()