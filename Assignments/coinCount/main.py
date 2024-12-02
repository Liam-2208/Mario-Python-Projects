import os
import math

#def display_bags() -> None:
    #code goes here

#def calculate_weight() -> int:
    #code goes here

def load_data():
    SPACING = 7

    coin_data: dict[str, list[str]] = {}
    if not os.path.exists("./coinCount.txt"): # Check if file exists
        os.system('' if os.name == 'nt' else 'touch coinCount.txt')  # If file does not exist, create it
        with open("coinCount.txt", "w") as data:
            data.write(f"Volunteer{SPACING*' '}Coin{SPACING*' '}Bag_Weight{SPACING*' '}Is_Correct") # Write default data to file
    else:
        with open("coinCount.txt", "r") as data: # If file does exist, dump data into a dictionary
            next(data) # Skip header line
            for line in data:
                arr = line.split(" "*SPACING) # Split line by removing spaces
                print(arr)     
                key: string = arr[0] # Set volunteers name as key
                if key not in coin_data: 
                    coin_data[key] = arr[1:4]
    return coin_data #key[name] = coin, key[1] = weight, key[2] = is_correct

def main() -> None:
    coin_data: dict[str, list[str]] = load_data()


    print(coin_data[])    
            
main()