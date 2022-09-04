import random

def ChoiceGame(Number, Times):


    while Times > 0:

        NumberChoice = int(input("Which number i choiced?: "))

        if(NumberChoice == Number):
            print(f"Congratulations, you got it right, the number is {NumberChoice}")
            break

        elif(NumberChoice != Number):
            Times = Times - 1
            print(f"You wrong, you have more {Times} chances")



print("Add numbers for me guess")

Number1 = int(input("Please choice a number: "))
Number2 = int(input("Thanks, now another number: "))

Number = random.randint(Number1, Number2)
Times = 3

ChoiceGame(Number, Times)       