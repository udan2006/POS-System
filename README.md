# 📦 Point of sale system - (POS System)

## 📖 Description

This is a simple **Point of Sale (POS)** system implemented in Python. The system allows users to manage a shopping basket, generate bills, search for previous bills, and generate tax transaction reports. It's designed to handle basic retail operations including adding items, updating quantities and prices, applying discounts, and generating a trasaction file.

---

## ✨ Key Features

| Feature Category         | Description                                                                                                                                             |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 🛒 **Basket Management** | - Add items with codes, prices, discounts, and quantities  <br> - View all basket items  <br> - Remove items by line number  <br> - Update item details |
| 🧾 **Billing System**    | - Generate formatted bills with line items and grand total  <br> - Automatic bill numbering  <br> - Search previous bills by bill number                |
| 📊 **Transaction file**  | - Generate CSV tax transaction file with checksum validation                                                                                            |
| ✅ **Data Validation**    | - Input validation for all numeric fields  <br> - Checksum calculation for data integrity in tax file                                                   |

---

## 💡 Example Interaction

- Add items: Add items to the bascket 
- Display item: Display all the items in the bascket
- Remove item: Remove item from the bascket 
- Update item: Update item in the bascket 
- Genarate bill: genarate bill number and add all items to the bill
- Search bill: Search bill with the bill number 
- Genarate tax transaction file: Calculate the checksum and write CSV file