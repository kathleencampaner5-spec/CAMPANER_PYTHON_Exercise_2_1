orders = []


def add_order(item_number, quantity):
    from menu import menu_items

    if item_number not in menu_items:
        return False

    if quantity <= 0:
        return False

    name, price = menu_items[item_number]

    orders.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    return True


def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total