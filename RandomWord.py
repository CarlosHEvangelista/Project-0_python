import random

FirstWord = str(input("Please enter a name: "))
SecondWord = str(input("Please enter a name: "))
ThirdWord = str(input("Please enter a name: "))
FourtyWord = str(input("Please enter a name: "))

WordList = [FirstWord, SecondWord, ThirdWord, FourtyWord]
Randomizer = random.choice(WordList)
Chances = 4


for Word in WordList:
    Response = str(input("Which word i choice?: "))

    if(Response == Randomizer):
        print(f"Congratulations, the word is {Randomizer} in the position {WordList.index(Randomizer) + 1}")
        break
    else:
        Chances = Chances - 1
        print(f"You fail, you have more {Chances} chances")
    
    if(Chances == 0):
        print("You lost yours chances")
        break

    