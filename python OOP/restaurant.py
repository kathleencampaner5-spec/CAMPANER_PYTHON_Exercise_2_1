class MenuItem:
    def __init__(self, item_number, name, price):
        self.item_number = item_number
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_subtotal(self):
        return self.menu_item.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        if quantity <= 0:
            return False

        order_item = OrderItem(menu_item, quantity)
        self.items.append(order_item)
        return True

    def get_total(self):
        total = 0

        for item in self.items:
            total += item.get_subtotal()

        return total

    def display_receipt(self):
        print("\n====================================")
        print("              RECEIPT")
        print("====================================")

        if not self.items:
            print("No orders yet.")
        else:
            for item in self.items:
                subtotal = item.get_subtotal()

                print(
                    f"{item.menu_item.name} x{item.quantity}"
                    f" - ₱{subtotal:.2f}"
                )

            print("------------------------------------")
            print(f"TOTAL: ₱{self.get_total():.2f}")

        print("====================================")


class Restaurant:
    def __init__(self):
        self.menu = [
            MenuItem(1, "Burger", 50.00),
            MenuItem(2, "Pizza", 120.00),
            MenuItem(3, "Fried Chicken", 100.00),
            MenuItem(4, "French Fries", 60.00),
            MenuItem(5, "Soft Drink", 30.00)
        ]

        self.order = Order()

    def display_menu(self):
        print("\n====================================")
        print("               MENU")
        print("====================================")

        for item in self.menu:
            print(
                f"{item.item_number}. "
                f"{item.name} - ₱{item.price:.2f}"
            )

        print("====================================")

    def add_order(self):
        self.display_menu()

        try:
            item_number = int(input("\nEnter item number: "))
            quantity = int(input("Enter quantity: "))

            selected_item = None

            for item in self.menu:
                if item.item_number == item_number:
                    selected_item = item
                    break

            if selected_item is None:
                print("\nInvalid item number.")
                return

            if self.order.add_item(selected_item, quantity):
                print("\nOrder added successfully!")
                self.order.display_receipt()
            else:
                print("\nInvalid quantity.")

        except ValueError:
            print("\nPlease enter numbers only.")

    def run(self):
        while True:
            print("\n====================================")
            print("       RESTAURANT ORDERING SYSTEM")
            print("====================================")
            print("1. View Menu")
            print("2. Add Order")
            print("3. View Receipt")
            print("4. Exit")
            print("====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_menu()

            elif choice == "2":
                self.add_order()

            elif choice == "3":
                self.order.display_receipt()

            elif choice == "4":
                print("\nThank you for ordering!")
                print("Goodbye!")
                break

            else:
                print("\nInvalid choice. Please select 1-4.")