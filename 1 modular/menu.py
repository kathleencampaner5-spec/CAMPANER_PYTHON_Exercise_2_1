menu_items = {
    1: ("Burger", 80),
    2: ("Fried Chicken", 120),
    3: ("Spaghetti", 100),
    4: ("French Fries", 60),
    5: ("Soft Drink", 40)
}


def display_menu():
    print("\n========== RESTAURANT MENU ==========")

    for number, item in menu_items.items():
        name, price = item
        print(f"{number}. {name} - ₱{price:.2f}")

    print("=====================================")