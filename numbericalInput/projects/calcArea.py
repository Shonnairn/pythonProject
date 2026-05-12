import math

# Giving a float to the user's input
radius = float(input("Enter the radius of a circle: "))

# math.pi is needed for the equation. However pow() is smarter but "**" is also an option!
area = math.pi * pow(radius, 2)

# Output of the equation for the user
# Okay so wasnt sure what the second argument for round() was.
# What is does is asking how many decimal places you want shown to the user.
# You can either put 1 or 2. No number will just give you a full number!
print(f"The area of the circle is: {round(area, 2)}cm²")
