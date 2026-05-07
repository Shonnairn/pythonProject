
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