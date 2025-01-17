import random

weapons = ["Fist","Knife","Club", "Gun", "Bomb", "Nuclear bomb"]
diceNumbers =[1,2,3,4,5,6]

input("Roll the dice: ")
weaponRoll = random.choice(diceNumbers)
print("You Rolled: " + str(weaponRoll))

heroStrength = weapons[weaponRoll]

print("Your weapon is: " + heroStrength)

if weaponRoll <= 2:
 print("Weak weapon")
elif weaponRoll <= 4:
  print("Your weapon is meh")

else:
  print("Powerful weapon!!")

if heroStrength != "Fist":
  print("Thank goodness you didn't roll the Fist")
else:
  print("Good Decision!!")





# LAB 02
