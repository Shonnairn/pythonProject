# Exercise 2 Shopping Cart Program

item = input("What item are you looking for?: ")
price = float(input(f"What is the price tag for your {item}?: "))
quantity = int(input(f"For how many {item}s are you looking into buying today?: "))

total = price * quantity

print(f"For {quantity} {item}(s). The total price will be ${total}.")