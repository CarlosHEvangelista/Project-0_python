import random

Number1 = int(input("Please enter a number: "))
Number2 = int(input("Now other number: "))

Number = random.randint(Number1, Number2)

chances = 1
Response = False

while Response != True:

    NumberChoice = int(input("Which number you think that i choice: "))


    if(NumberChoice > Number):
        print("You wrong, the number is lower")
        chances = chances + 1
        
    elif(NumberChoice < Number):
        print("You wrong, the number is higher")
        chances = chances + 1

    elif(NumberChoice == Number):
        print(f"You got it, the number is {Number}, you attempts: {chances}")
        Response = True
