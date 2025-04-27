import csv

from model.bascket import Basket
from model.bill import Bill
from model.checkSum import checkSum


class Basket_Manager:
    barscket = []
    bill = {}
    lineNumber = 0
    billNumber = 1000

    def add_to_bascket(self, item_code, internal_price, discount, quantity, sales_price):

        for item in self.barscket:
            if item.item_code == item_code:
                print("If you want to update go to the update category.")
                return

        self.lineNumber += 1
        items = Basket(self.lineNumber, item_code, internal_price, discount, quantity, sales_price)
        self.barscket.append(items)

    def showBascket(self):
        if len(self.barscket) == 0:
            print("No items added to basket")
            return
        else:
            print("-" * 100)
            print(
                f"{"line Number":<15} {"Item Code":<18} {"Internal price":<18} {"Qty":<8} {"Discount":<10} {"Sales price":<15} {"Line total":<10}")
            print("-" * 100)

            for item in self.barscket:
                print(
                    f"{item.lineNumber:<15} {item.item_code:<18} {item.internal_price:<18} {item.quantity:<8} {item.discount:<10} {item.sales_price:<15} {item.line_total:<10}")
                print("        ")

    def remove_item(self, lineNumber):
        for item in self.barscket:
            if item.lineNumber == lineNumber:
                self.barscket.remove(item)
                print(f"Item removed from basket: {lineNumber}")
                return
        print(f"Item not found in basket: {lineNumber}")

    def update_item(self, lineNumber):
        for item in self.barscket:
            if item.lineNumber == lineNumber:
                while True:
                    try:
                        print("""================= Update Menu Bar =================
                        1. Sale Price 
                        2. Discount 
                        3. Quantity 
                        4. Exit""")

                        choice_in = input("Enter your choice: ")
                        if not choice_in.isdigit() or not 1 <= int(choice_in) <= 4:
                            print("Please enter a valid choice.")
                            continue
                        choice = int(choice_in)

                        if choice == 1:
                            try:
                                new_price = float(input("Enter new price: "))
                            except ValueError:
                                print("Please enter a valid price.")
                                continue

                            item.sales_price = new_price
                            item.line_total = new_price * item.quantity
                            print(f"Item slaes price updated in the lineNumber : {lineNumber}")
                            continue
                        elif choice == 2:
                            try:
                                new_discount = float(input("Enter new discount: "))
                            except ValueError:
                                print("Please enter a valid discount.")
                                continue

                            item.discount = new_discount
                            print(f"Item discount updated in the lineNumber : {lineNumber}")
                            continue
                        elif choice == 3:
                            try:
                                new_quantity = int(input("Enter new quantity: "))
                            except ValueError:
                                print("Please enter a valid quantity.")
                                continue

                            item.quantity = new_quantity
                            print(f"Item quantity updated in the lineNumber : {lineNumber}")
                            continue
                        elif choice == 4:
                            print("Thank you!")
                            break
                        else:
                            print("Invalid choice")
                            continue
                    except Exception as e:
                        print("Error occurred: " + e)

    def genarate_bill(self):
        if not self.barscket:
            print("No items added to basket")
            return

        grand_total = 0
        for item in self.barscket:
            grand_total += item.line_total

        self.billNumber += 1

        new_bill = Bill(self.billNumber, self.barscket.copy(), grand_total)

        self.bill[self.billNumber] = new_bill

        new_bill.display_bill()

        self.barscket.clear()
        self.lineNumber = 0

    def search_bill(self, billNumber):
        if billNumber in self.bill:
            bill = self.bill[billNumber]
            bill.display_bill()
        else:
            print(f"Bill number {billNumber} not found in basket.")

    def generate_tax_transaction(self):
        file_name = "all_tax_transactions.csv"

        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Bill Number", "Item Code", "Internal Price", "Discount", "Sales price", "Quantity", "Checksum"])

            for bill_number, bill in self.bill.items():
                for items in bill.item:
                    values = [
                        str(bill_number),
                        items.item_code,
                        str(items.internal_price),
                        str(items.discount),
                        str(items.sales_price),
                        str(items.quantity),
                    ]

                    raw_line = ",".join(values)
                    check = checkSum(raw_line)
                    checkSum_eachLine = check.calculate()

                    writer.writerow(values + [str(checkSum_eachLine)])
        print("tax file successfully generated.")
