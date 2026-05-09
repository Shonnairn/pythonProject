# if = do some code only IF some conditions is True
# Else do something else

age = int(input("Enter your age:"))

if age >= 100:
    print("You're too old to sign up.")
if age >= 18:
    print("You are now signed up for a bank account!")
elif age <= 13:
    print("You're too young to sign up for an account.")
else:
    print("Unfortunately, you're not old enough to sign up for an account. Please come back when you're 18.")

