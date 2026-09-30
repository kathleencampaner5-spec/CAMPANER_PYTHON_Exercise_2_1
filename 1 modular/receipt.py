import order


def display_receipt():
    print("\n========== RECEIPT ==========")

    if len(order.orders) == 0:
        print("No orders placed.")
        print("=============================")
        return

    for item in order.orders:
        subtotal = item["price"] * item["quantity"]

        print(
            f"{item['name']} x {item['quantity']} "
            f"= ₱{subtotal:.2f}"
        )

    print("-----------------------------")
    print(f"TOTAL: ₱{order.calculate_total():.2f}")
    print("=============================")
    print("Thank you for ordering!")