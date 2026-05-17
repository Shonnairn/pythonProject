# Validate user input exercise
# 1) username is no longer than 12 characters long
# 2) username must not contain spaces
# 3) username will not have digits

username = input("Enter a username: ")

username.find(" ")

if len(username) > 12:
    print("Your username can't be no longer than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username must not contain spaces.")
    
    # .isalpha() can do the same for finding spaces. However .find() would be best just for as a catcher like JS
elif not username.isalpha():
    print("Your username must not contain digits.")
else:
    print(f"Welcome {username.capitalize()}!")