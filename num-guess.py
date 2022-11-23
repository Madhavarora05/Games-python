print("Welcome to Number guessing game ")
print("How to play:- You just have to guess a number b/w 1 to 20 and you have only 5 tries.")
import random
n=random.randint(1,20)
tries=0
while tries<5:
    guess=int(input("Enter an integer from 1 to 20:-"))
    tries+=1
    if guess<n:
        print("Your guess is too low")
    if guess>n:
        print("Your guess is too high")
    if guess==n:
        break
if guess==n:
        print("Congatulations, you have guessed correct in",tries,"tries!!")
else:
    print("Game over you were not able to guess the correct")
    print("The correct answer was", n)