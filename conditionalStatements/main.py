# Conditional Expression = A one-line shortcut for the if-else statement (ternary operators)
# Print or assign one of two values based on a condition
# X if condition else Y


# From better understanding the ascept is in the fact using if and else.
# Were using <, >, and =, for numbers
# Or matching written strings. referring to the admin accees
# Sounds simple enough


num = 5
print ("Positive" if num > 0 else "Negative")

num = 2
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7

max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 21
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 30
weather = "HOT" if temperature > 20 else "COLD"
print(weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)