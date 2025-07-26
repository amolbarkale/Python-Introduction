TAX_RATE = 0.085  # 8.5% tax
items = []
subtotal = 0

for i in range(1, 4):
    price = float(input(f"Enter price of item {i}: "))
    quantity = int(input(f"Enter quantity of item {i}: "))
    total = price * quantity
    
    subtotal += total
    items.append((i, price, quantity, subtotal))

TAX = subtotal * (TAX_RATE / 100)
final_total = subtotal + TAX

print("\n--- Receipt ---")
for item in items:
    i, price, qty, total = item
    print(f"Item {i}: ₹{price:.2f} × {qty} = ₹{total:.2f}")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax (8.5%): ₹{tax:.2f}")
print(f"Total: ₹{final_total:.2f}")