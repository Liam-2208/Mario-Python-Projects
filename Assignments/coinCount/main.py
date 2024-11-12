import os
import math
import json
import time

def clear_console():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') 

def load_data(): #Writes contents of txt to JSON
    with open("coinCount.txt", "r") as data_txt: 
        with open("data.json", "w") as data_json: 
            for line in data_txt:
                data_json.writelines(line)
    

def main() -> None:
    load_data()
    valid_coins = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.01]

    name: str = input("Enter name: ")
    try:
        coin: float = float(input(f"Valid Coins: {valid_coins}\nEnter coin: "))
        while coin not in valid_coins:
            print("Coin not valid.")
            clear_console()
            coin: float = float(input(f"Valid Coins: {valid_coins}\nEnter coin: "))
    except (TypeError, ValueError):
        print("Coin should be of type float, eg: £2 = 2.0")
        clear_console()
    
    while True:
        try:
            weight: int = int(input("Enter weight: "))
            break
        except (TypeError, ValueError):
            print("Value should be of type int.")
            clear_console()

    
    coin_data: dict[str, dict[str, float, int, bool]] = {
        f"{coin}":
            {
            "name": name,
            "coin": coin,
            "weight": weight,
            "is_correct": False
            }
        }
    
    with open("data.json", "w") as data_json:
        data_json.writelines(json.dumps(coin_data, indent = 4))




    print(coin_data)    
            
main()