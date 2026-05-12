# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilograns or Pounds? (K/P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not valid.")