import random
import math

#Taking inputs
lower=int(input("enter the lower bound : "))
upper=int(input("enter the upper bound: "))

#Intialalizing
RandNum=random.randint(lower,upper)
NumberOfGuess=round(math.log(upper-lower+1,2))
print("You have",NumberOfGuess,"chances to guess the number")
GuessCount=0
#We make the logic
while GuessCount<NumberOfGuess:
    GuessCount+=1
    Guess=int(input("enter the number you guessed: "))
    if Guess==RandNum:
        print("congratulations you did it in",GuessCount,"tries")
        break
    elif Guess<RandNum:
        print("you gussed too small")
    elif Guess>RandNum:
        print("You guessed to big")
if GuessCount>=NumberOfGuess:
    print("hard luck the number was",RandNum)
    print("better luck next time")
    




