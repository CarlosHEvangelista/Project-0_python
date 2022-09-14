import random

RandomWords = ["Bananas", "Apples", "Coffe", "Watermelon", "Pizza", "Pineapple"]

SelectWord = random.choice(RandomWords)


HiddenWord = SelectWord

HiddenWord = list(HiddenWord)
for Letter in HiddenWord:
    HiddenWord = ''.join(HiddenWord)
    HiddenWord = HiddenWord.replace(Letter, "*")


Changes = 6

while Changes > 0:

    SelectLetter = input("Tell me a letter: ")
    index = 0

    while index <= len(SelectWord):
        SelectWord = ''.join(SelectWord)

        Position = SelectWord.find(SelectLetter, index)
        

        SelectWord = list(SelectWord)

        if(SelectWord[Position] == SelectLetter):
            HiddenWord = list(HiddenWord)
            HiddenWord[Position] = SelectLetter
            if(HiddenWord.count(SelectLetter) == SelectWord.count(SelectLetter)):
                print(HiddenWord)
                break

        else:
            print("You fail, try again")        
            Changes = Changes - 1
            break
        index += 1
    HiddenWord = ''.join(HiddenWord)
    if(HiddenWord.find("*") == -1):
        print("Congratulations")
        break


