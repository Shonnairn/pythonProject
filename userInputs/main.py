# input() is the function that lets the user type for a question or just filling a prompt.
# This does also return as a string fyi.

name =input("Do you have a name?: ")
age = int(input("What's your age?:"))

# age = (age) + 1

# Remeber in order to change numberic values. Converting it into a float or int is required.

# age = int(age) + 1

#However putting the int() function can be wrapped around the input. Think of it as a wrapper around a wrapper.

print(f"Hey there, {name}!")
print("Happy birthday!")
print(f"Oh wow! You're {age} years old?!")