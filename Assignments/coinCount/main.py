import os
import math

#def display_bags() -> None:
    #code goes here

#def calculate_weight() -> int:
    #code goes here

def load_data():
    coin_data: dict[str, list[str, float, bool]] = {}
    if not os.path.exists("./coinCount.txt"): # Check if file exists
        os.system('' if os.name == 'nt' else 'touch coinCount.txt')  # If file does not exist, create it
        with open("coinCount.txt", "w") as data:
            data.write(f"Volunteer{SPACING*' '}Coin{SPACING*' '}Bag_Weight{SPACING*' '}Correct") # Write default data to file
    else:
        with open("coinCount.txt", "r") as data: # If file does, exist, dump data into a dictionary
            next(data) # Skip header line
            for line in data:
                arr = line.split(" "*SPACING) # Split line by removing spa
                print(arr)     
                key: string = arr[0] # Set volunteers name as key
                if key not in coin_data: 
                    coin_data[key] = arr[1:4]

def update_data():
    

def main() -> None:
    SPACING = 7 # Amount of spacing between elements in .txt file
    coin_data: dict[str, list[str, float, bool]] = load_data()



    print(coin_data)    
            
main()