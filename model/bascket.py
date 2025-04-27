class Basket:
    def __init__(self,lineNumber,item_code, internal_price, discount, quantity, sales_price):
        self.lineNumber = lineNumber
        self.item_code = item_code
        self.internal_price = internal_price
        self.discount = discount
        self.quantity = quantity
        self.sales_price = sales_price
        self.line_total = sales_price * quantity


    def __repr__(self):
        print(self.item_code)
        print(self.internal_price)
        print(self.discount)
        print(self.quantity)
        print(self.sales_price)
        print(self.line_total)
