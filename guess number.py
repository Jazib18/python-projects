# Guess the correct Number Game

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the Target or Quit(Q) :")
    if(userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too Small. Take a Bigger Guess")
    else:
        print("Your number was to Large. Take a smaller Guess")

print("-----GAME OVER-----")
