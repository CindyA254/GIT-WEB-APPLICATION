# Cashier program to calculate the total bill
total_bill = 0

print("Welcome to the Grocery Store!")
print("Scan items and type 'done' when finished.")

while True:
    item = input("Scan item or type 'done' to finish: ")

    if item.lower() == 'done':
        break  # Exit the loop if the cashier types 'done'

    try:
        price = float(input("Enter the price of the item: "))
        total_bill += price  # Add the price of the item to the total bill
    except ValueError:
        print("Invalid input. Please enter a valid price.")

print(f"Total bill: ${total_bill:.2f}")
print("Thank you for shopping with us!")
