import random

Name=input('enter your name: ')

Words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(Words)

guesses=""

turns=12
print('Good luck',Name)
while turns>0:
    

    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed=failed+1
    print()
    guess=input("guess a character: ")
    guesses+=guess
    if failed==0:
        print("you win the word is : ",word)
        break
    if guess not in word:
        turns-=1
        print("wrong you have",turns,"guesses")
    if turns==0:
        print("you loose")
        
