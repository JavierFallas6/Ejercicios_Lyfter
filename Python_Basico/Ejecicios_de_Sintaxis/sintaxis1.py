product_price = float(input("Insert product price "))

if (product_price < 100):
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

final_price = product_price - discount
print(f"{final_price} is the total")
