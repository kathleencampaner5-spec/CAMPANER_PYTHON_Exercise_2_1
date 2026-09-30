import menu
import order
import receipt


def main():
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
            menu.display_menu()

        elif choice == "2":
            menu.display_menu()

            try:
                item_number = int(input("\nEnter item number: "))
                quantity = int(input("Enter quantity: "))

                if order.add_order(item_number, quantity):
                    print("\nOrder added successfully!")
                else:
                    print("\nInvalid item number or quantity.")

            except ValueError:
                print("\nPlease enter numbers only.")

        elif choice == "3":
            receipt.display_receipt()

        elif choice == "4":
            print("\nThank you for ordering!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()