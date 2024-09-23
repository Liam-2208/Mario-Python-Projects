import time

def payment(credit, valid_coins, items, choice):
    while credit < items[choice][1]:
        try:
            print(f"\nItem selected: {items[choice][0]}")
            coin = float(input(f"Amount due: {round((items[choice][1] - credit), 2)}\nCoins Accepted: {valid_coins}\nInsert Coins: "))
            if coin not in valid_coins:
                print("Coin not accepted.")
                time.sleep(2)
            else:
                credit+=coin
        except ValueError:
            print("Enter coin as a float.\n")
            time.sleep(1)

    if credit > items[choice][1]:
        print(f"You have {round((credit - items[choice][1]), 2)} in change")
        print(f"{items[choice][0]} has been dispensed.")
    else:
        print(f"{items[choice][0]} has been dispensed.")


def main():
    credit = 0
    choice = ""
    valid_coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2]
    items = {
        "A1": ["Original", 1.55],
        "A2": ["Ultra White", 1.45],
        "B1": ["Ultra Rosa", 1.50],
        "B2": ["Bad Apple", 1.60],
        "C1": ["Orange Dreamsicle", 1.60],
        "C2": ["Ultra Strawberry Dreams", 1.65],
        "D1": ["Ultra Paradise", 1.45],
        "D2": ["Khaotic", 1.50]
    }

    print("Items:")
    for key in items:
        print(f"{key}: {items[key]}")
    choice = input("Please pick an item: ")
    choice = choice.capitalize()
    if choice not in items:
        print("Please choose a valid choice.\n")
        time.sleep(1)
        main()
    payment(credit, valid_coins, items, choice)
    main()


main()