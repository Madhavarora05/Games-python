import random
name=input("What is your name")
print("Good luck!",name)
words=['creta','venue','seltos','sonet','ertiga','swift','nano','rangerover','safari','nexon','hondacity','fortuner']
word=random.choice(words)
print("Guess the character")
guesses=''
turns=10
while turns>5:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print(" _")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    guess =input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
        if turns == 0:
              print("You Loose")
