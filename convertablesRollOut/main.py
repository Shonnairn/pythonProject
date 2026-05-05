# Now this is actually new to me. JS does not have Typecasting.
# Or maybe it does but im not sure.

name = "John"
age = 22
gpa = 4.45
is_student = True

type(name)
type(age)
type(gpa)
type(is_student)

# This will all show its data type. However it will not show anything so you must put a print before it

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Now for floats I can actually convert it into a whole number and vise versa.

gpa = int(gpa)
age = float(age)

print(gpa)
print(age)

# Both of this can be converted into a string too
gpa = str(gpa)
age = str(age)

print(gpa)
print(age)

# Now strings into Booleans. This is just like JS and its pretty cool too!

is_student = bool(is_student)

print(is_student)

# As long there is a value of character it will be true.

is_student = bool("")
print(is_student)

# However no character will be false. Handy for when forms.
