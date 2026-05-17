# Indexing = accessing elements of a sequence using [] (indexing operator) 
# [ start : end : step ]

creditNumber = "1234-5678-9012-3456"

# So this will print whatever character is in the string starting from zero.
# Its a singular character return.
print(creditNumber[0])

# However looking at the top. If i want to print a sentence/sequence. I have to
# Have a start which is 0 or anywhere else. Seperate it with a colon ":" and 
# Choose where I want to end.
print(creditNumber[0:14])
print(creditNumber[5:19])
# A zero isnt a must either. This line of code will run 
# because python assumes i need everything from the start
print(creditNumber[:19])
# Same goes the other way around. Maybe I want to start from the
# 10th character and need the rest
print(creditNumber[10:])
# Now if the very last character is important we can run this line
print(creditNumber[-1])
# This rule can be increased by going backwards. Think of it as x,y,z formula
# Everything else with negative is the same as postive rules

# The step argument is character skips. Here its every "2" we get a return back
print(creditNumber[::2])

lastDigits = creditNumber[-4:]

print(f"XXXX-XXXX-XXXX-{lastDigits}")

# We can also flip the string into being reversed if we liked to
creditNumReversed = creditNumber[::-1]
print(creditNumReversed)