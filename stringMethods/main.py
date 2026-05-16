name = input("Enter your name: ")
phoneNumber = input("Enter your phone number: ")

result = len(name)
#This is to find any character that is the first
result2 = name.find(" ")
#This is to find the last of said character
result3 = name.rfind("a")
#This will force the first character in the string to be well capitalized
name = name.capitalize()
#Creates all letters to be uppercase
name = name.upper()
#Creates all letters to be lowercase
name = name.lower()
#It is a boolean for only numbers. can't have any characters
result = name.isdigit()
#Boolean as well for ONLY letters. excluding spaces as well.
result = name.isalpha()

result = phoneNumber.count("-")

#Will be handy for when we need to replace any characters from a user's input
phoneNumber.replace("-", "")

# FYI we can always run this too!
print(help(str))