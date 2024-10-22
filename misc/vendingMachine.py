import time
import os

def dispense(item, credit):
    if credit > 0:
        print(f"You have {round(credit, 2)} in change")
    print(f"{item} has been dispensed.")
    time.sleep(1)

def payment(items, selected_item):
    credit = 0
    valid_coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
    amount_due = items[selected_item][1]
    item = items[selected_item][0]
    while credit < amount_due:
        os.system("cls")
        try:
            print(f"\nItem selected: {item}")
            amount_due = items[selected_item][1] - credit
            coin = float(input(f""""Amount due: {round(amount_due, 2)}\n
            Coins Accepted: {valid_coins}\nInsert Coins: """))
            if coin not in valid_coins:
                print("Coin not accepted.")
                time.sleep(1)
            else:
                credit += coin
        except ValueError:
            print("Enter coin as a float.\n")
            time.sleep(1)

    credit = credit - items[selected_item][1]
    return credit

def select_item(items):
    print("Items:")
    for key in items:
        print(f"{key}: {items[key]}")
    selected_item = input("Please pick an item: ")
    selected_item = selected_item.capitalize()
    
    while selected_item not in items:
        print("Please choose a valid choice.\n")
        time.sleep(1)
        os.system("cls")
        for key in items:
            print(f"{key}: {items[key]}")
        selected_item = input("\nPlease pick an item: ")
        selected_item = selected_item.capitalize()
    return selected_item

def main():
    choice = ""
    items = {
        "A1": ["Original", 1.55, ],
        "A2": ["Ultra White", 1.45],
        "B1": ["Ultra Rosa", 1.50],
        "B2": ["Bad Apple", 1.60],
        "C1": ["Orange Dreamsicle", 1.60],
        "C2": ["Ultra Strawbery Dreams", 1.65],
        "D1": ["Ultra Paradise", 1.45],
        "D2": ["Khaotic", 1.55]
    }
    selected_item = select_item(items)
    os.system("cls")
    credit = payment(items, selected_item)
    os.system("cls")
    dispense(selected_item, credit)

if __name__ == "__main__":
    main()