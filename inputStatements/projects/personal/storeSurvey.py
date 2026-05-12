# Personal excerise of madlibs

print("Thank you for taking the time to fill out this survery!")

name = input("What is your name?: ")
employeeName = input("What is the name of the employee who assisted you today?: ")
service = float(input(f"On a scale of 1-10, how would you rate the service from {employeeName}?: "))
adjective1 = input("Please describe your experience with one adjective: ")
adjective2 = input("Please describe your experience with another adjective: ")
customerComment = input("Was there anything you'd like to share about your experience today?: ")

print(f"Thank you for your feedback, {name}! We're glad {employeeName} was able to assist you today. Your rating of {service} and your comments about the service being {adjective1} and {adjective2} are greatly apreciated. Have an amazing day!")
