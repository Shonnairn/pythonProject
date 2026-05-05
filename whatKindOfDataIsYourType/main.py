# Variable = It is basically a container for storing data values. 
#            It is a fundamental concept in programming that allows you to store and 
#            manipulate data in your code.

# This below is what you call the "string" data type.
# We call them characters. However, numbers can be store in here as well.
first_name = "John"
food = "pizza"
email = "email@example.com"

print(f"The name is {first_name}.")
print(f"Personally, I do not mind {food}!")
print(f"However, if you believe that's dumb? Feel free to reach out to me at {email}!")

# As for intergers, they're what we identify numbers in code.
age = 22
quantity = 2
num_of_students = 0

print(f"You're at least {age} years old!")
print(f"Do you want to buy a total of {quantity} laptops?")
print(f"Imagine having {num_of_students} students who failed the quiz? Couldn't be me!")

# Floats are intergers however they are the equivalent to decimals
price_of_stove = 5034.99
gpa = 3.75
marathon_distance = 26.2

print(f"Our stove is actually on sale for ${price_of_stove} dollars! What a steal!")
print(f"I think my gpa was around {gpa}")
print(f"Did you know I actually ran a total of {marathon_distance} miles in the LA marathon in 2020?")

# Booleans is a data type of either 1 or 2. True or false

is_student = False
is_kitchenAid_on_promos = True
is_online = False

if is_student:
    print("Shonnairn is currently a student.")
else:    
    print("Shonnairn is not currently a student.")
# print(f"Is shonnairn a student currently? {is_student}")

if is_kitchenAid_on_promos:
    print("KitchenAid is currently on promos!")
else:
    print("KitchenAid does not have any ongoing promotions currently.")

if is_online:
    print(f"Shonnairn currently just went live!")
else:
    print(f"Shonnairn is currently offline.")

# Now the me portion of using all of these together!

company_name = "Retail Inc."
minimum_wage = 15
store_rating = 4.2
is_hiring = False

if is_hiring:
    print(f"{company_name} is currently hiring! We've got a store rating of {store_rating} stars. Plus, we pay a minimum wage of ${minimum_wage} dollars hourly! What are you waiting for? Apply today!")
else:
    print(f"{company_name} unfortunately is not hiring. Feel free to shop here since our store provides the best service. After all, we've got a total of {store_rating} stars!")