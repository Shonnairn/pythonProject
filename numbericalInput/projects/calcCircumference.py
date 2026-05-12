import math

# User input for the radius
radius = float(input("Enter the radius of the circle: "))

# We're using the math.pi constant and the radius
circumference = 2 * math.pi * radius

# Output is the total with also multiplying by 2 for the full sizing
print(f"The circumference is: {round(circumference, 2)}cm")