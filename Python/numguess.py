#now we're creating a number guessing game kind of thing ig?....let's get started
import random
difficulty=input("Choose the difficulty:{EASY,MEDIUM,HARD}:")
difficulty=difficulty.upper()
if difficulty=="EASY":
    code=random.randint(1,10)
    print("I'm thinking of a number between 1 and 10")
elif difficulty=="MEDIUM" :
    code=random.randint(1,50)
    print("I'm thinking of a number between 1 and 50")
elif difficulty=="HARD":
    code=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")
else: 
    print("INVALID DIFFICULTY!") 
    exit()
num=int(input("Think you can guess it? Take a guess:"))
attempt=1
while num != code:
    if num<code : print("Too low.")
    elif num>code: print("Too high.")
    num=int(input("Guess agian:"))
    attempt+=1
else: print("Correct!")
print("Attempts:",attempt)

