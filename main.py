from model.functions import Basket_Manager

manage = Basket_Manager()

while True:
    try:
        print("=========== Menu bar ===============")
        print("1. Add items to the bascket.")
        print("2. Display the Bascket.")
        print("3. remove item from the bascket.")
        print("4. update item in the bascket.")
        print("5. Genarate Bill.")
        print("6. Search Bill.")
        print("7. Generate tax file")
        print("8. exit the program")
        print("  ")

        choice_input = input("Enter your choice: ")
        if not choice_input.isdigit() or not 1 <= int(choice_input) <= 8:
            print("Invalid choice. Please enter a valid choice.")
            continue

        choice = int(choice_input)

        if choice == 1:
            item_code = input("Enter the item code: ")
            try:
                internal_price = float(input("Enter the internal price: "))
                discount = float(input("Enter the discount: "))
                quantity = int(input("Enter the quantity: "))
                sales_price = float(input("Enter the sales price: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            manage.add_to_bascket(item_code, internal_price, discount, quantity, sales_price)
            manage.showBascket()
            continue
        elif choice == 2:
            manage.showBascket()
            continue
        elif choice == 3:
            try:
                removeLineNumber = int(input("Enter the line number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            manage.remove_item(removeLineNumber)
            continue
        elif choice == 4:
            try:
                updateLineNumber = int(input("Enter the line number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            manage.update_item(updateLineNumber)
            continue
        elif choice == 5:
            manage.genarate_bill()
            continue
        elif choice == 6:
            try:
                billNumber = int(input("Enter the bill number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            manage.search_bill(billNumber)
            continue
        elif choice == 7:
            manage.generate_tax_transaction()
        elif choice == 8:
            print("Thank you!")
            break

    except Exception as e:
        print("Error occurred: " + e)

