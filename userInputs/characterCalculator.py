# Personal Exercise!

nameOfCharacter = input("What is the name of your character?: ")
attackPower = float(input("What's the attack power of your character?: "))
hitPoints = float(input("How much hp does your character have?: "))
manaPoints = float(input("What's the mp on your character?: "))
defense = float(input("How much defense do they have?: "))

# levelingUp = int({characterInfo} * 1.25)
# I thought this would work, but it throws an error.

#levelingUp = int(sum(characterInfo) * 1.25)

# Option 2 was multiplying within the array, but I guess its different compared to JS

# However with copilot it recommened to use sum() so ill test it out

# characterInfo = sum([attackPower, hitPoints, manaPoints, defense]) * 1.25

# Seems like I dont know so I'll come back to this when I have a better understanding how to solve this.

attackPower = attackPower * 1.25
hitPoints = hitPoints * 1.25
manaPoints = manaPoints * 1.25
defense = defense * 1.25
characterInfo = [attackPower, hitPoints, manaPoints, defense]

print(f"{nameOfCharacter} has just leveled up! This is the new stats: {characterInfo}.")