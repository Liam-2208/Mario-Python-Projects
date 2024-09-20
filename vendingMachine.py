def main():
    credit = 0
    valid_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    items = {
        "A1": ["Original", 1.55],
        "A2": ["Ultra White", 1.45],
        "B1": ["Ultra Rosa", 1.50],
        "B2": ["Bad Apple", 1.60],
        "C1": ["Orange Dreamsicle", 1.60],
        "C2": ["Ultra Strawbery Dreams", 1.65],
        "D1": ["Ultra Paradise", 1.45],
        "D2": ["Khaotic", 1.50]
    }

    for key in items:
        print(f"{key}: {items[key]}")

    coin = input(f"Please insert a coin.\nCoins accepted: {valid_coins}")

main()