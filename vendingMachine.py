import time

def dispense(item, credit):
    if credit > 0:
        print(f"You have {credit} in change")
        print(f"{item} has been dispensed.")
        time.sleep(1)
    else:
        print(f"You have no change.")
        print(f"{item} has been dispensed.")
        time.sleep(1)

def payment(credit, items, selected_item):
    valid_coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
    amount_due = items[selected_item][1]
    item = items[selected_item][0]
    while credit < amount_due:
        try:
            print(f"\nItem selected: {item}")
            amount_due = items[selected_item][1] - credit
            coin = float(input(f"Amount due: {round(amount_due, 2)}\nCoins Accepted: {valid_coins}\nInsert Coins: "))
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
        selected_item = input("\nPlease pick an item: ")
        for key in items:
            print(f"{key}: {items[key]}")
        time.sleep(1)
    return selected_item

def main():
    credit = 0
    choice = ""
    items = {
        "A1": ["Original", 1.55],
        "A2": ["Ultra White", 1.45],
        "B1": ["Ultra Rosa", 1.50],
        "B2": ["Bad Apple", 1.60],
        "C1": ["Orange Dreamsicle", 1.60],
        "C2": ["Ultra Strawbery Dreams", 1.65],
        "D1": ["Ultra Paradise", 1.45]
    }