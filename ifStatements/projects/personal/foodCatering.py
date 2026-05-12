# Today we're at a party doing a catering job. Let's make sure to have the menu right

cheese_Pizza = ["dough", "tomato sauce", "cheese"]
pepperoni_Pizza = ["dough", "tomato sauce", "cheese", "pepperoni"]
bbq_Chicken_Pizza = ["dough", "tomato sauce", "cheese", "bbq chicken"]
shrimp_Pizza = ["dough", "tomato sauce", "spinich", "shrimp"]

menu_list = [cheese_Pizza, pepperoni_Pizza, bbq_Chicken_Pizza, shrimp_Pizza]
pizza_names = ["Cheese Pizza", "Pepperoni Pizza", "BBQ Chicken Pizza", "Shrimp Pizza"]

print("Welcome to the party! What kind of pizza would you like?" \
"Current our option are: cheese pizza (1), pepperoni pizza (2), BBQ chicken pizza (3), and shrimp pizza (4)." )
order = int(input("Please enter the name of the pizza number you'd like to order: "))



if order <= 0:
    print("Please enter a valid option.")
elif order == 1:
    print(f"You've choosen: {pizza_names[0]}. It's recipe contains: {menu_list[0]}")
elif order == 2:
    print(f"You've choosen: {pizza_names[1]}. It's recipe contains: {menu_list[1]}")
elif order == 3:
    print(f"You've choosen: {pizza_names[2]}. It's recipe contains: {menu_list[2]}")
elif order == 4:
    print(f"You've choosen: {pizza_names[3]}. It's recipe contains: {menu_list[3]}")
else:
    print("This is not a valid option. Please enter what you'd like.")

user_Confirmation = input(f"If you're okay with your choose? (Y/N): ")

if user_Confirmation == "Y":
    print("Alrighty, your pizza will be done in 10 minutes!")
elif "N":
    print("Oh okay, feel free to look at the other orders!")
else:
    print("Sorry, that is not an option.")
    order

# I did want to add an option where the user could add and remove on their ingrediant but couldnt understand that but will keep in mind for the future!