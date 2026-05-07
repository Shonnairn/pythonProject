import math

x = 8.2

friends = 0

# friends = friends + 1
# This below is the same ruling like JS math
friends += 1

print(friends)

# friends = friends - 1
friends -= 2

print(friends)

#friends = friends * 4
friends *= 4

print(friends)

#friends = friends / 2
friends /= 2

print(friends)

friends = friends ** 3
friends **= 3

print(friends)

remainder = friends % 8

print(remainder)

# All of this is the basic math operators in Python.

# Addition, subtraction, multiplication, division, exponentiation, and lastly modulus.

# ----------------------------------------------------------------

x = 3.14
y = -2.71
z = 5

# The round() function here makes floating numbers into integers without calling the float() functions
result = round(x)

print(result)

# The abs() function returns the value of the number from 0. 
result2 = abs(y)
print(result2)

# pow() function is the power of a number. Needs to different arguments.
result3 = pow(z, x)
print(result3)

# max() and min() function return a certain value. Max will return the highest value while the min will return the lowest value.
result = max(x, y, z)
result = min(x, y, z)

print(result)

# So Python actually does use the import like JS too!

print(math.pi)
# This will print the pi value. Not all of it just enough of it lol

print(math.e)
# It also even includes the scientific constant e!

result = math.sqrt(x)
# This function of course does the square root of a number.

result = math.ceil(x)
# Cieling function is actually rounding up a number

result = math.floor(x)
# Floor function is rounding down a number