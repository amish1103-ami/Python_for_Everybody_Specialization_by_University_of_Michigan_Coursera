# Get and validate notebook price
while True:
    try:
        price = float(input("Price of one notebook: ₹"))

        if price < 0:
            print("Error: Price cannot be negative.")
            continue

        break

    except ValueError:
        print("Error: Please enter a valid price.")


# Get and validate quantity
while True:
    try:
        quantity = int(input("Number of notebooks: "))

        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            continue

        break

    except ValueError:
        print("Error: Please enter a whole number for quantity.")


# Calculate total cost
total_cost = price * quantity

# Display receipt
print("\n------ Receipt ------")
print(f"Notebook price: ₹{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total cost: ₹{total_cost:.2f}")
