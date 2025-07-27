def display_cart(cart):
    print("Current cart contents:")
    for index, itm in enumerate(cart):
        print(f"{index}: {itm}")

cart = []

cart.append("apple")
cart.append("banana")
cart.append("apples")
cart.append("bread")
cart.append("milk")
cart.append("eggs")

if "bread" in cart:
    cart.remove("bread")

if cart:
    cart.pop()

cart.sort()

for item in cart:
    print(item)

display_cart(cart)