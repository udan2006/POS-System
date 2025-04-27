class Bill:
    def __init__(self,billNumber,item,total):
        self.billNumber = billNumber
        self.item = item
        self.total = total

    def display_bill(self):
        print(f"=========== Bill ${self.billNumber} ==========")
        print(f"{"Line number":<15} {"Item code":<10} {"Qty":<10} {"Discount":<10} {"Line total":<10}")
        print("="*60)

        for items in self.item:
            print(f"{items.lineNumber:<15} {items.item_code:<10} {items.quantity:<10} {items.discount:<10} {items.line_total:<10}")
        print("-"*60)

        print(f"Grand Total: Rs.{self.total}")
        print("=================================")
        print("      ")