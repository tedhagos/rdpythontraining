import random

maxNumber = 1000
randomNumber = random.randint(1, maxNumber) # generate a random num from 1 to maxNum
getOut = False
print(randomNumber)

try:
    guess = int(input("Can you guess the number ? 1 .. 1000 "))

    while not getOut:
        if guess == randomNumber:
            print("You guessed correctly. The number is {0}".format(randomNumber))
            getOut = True
            break
        elif guess > randomNumber:
            guess = int(input("lower "))
        else:
            guess = int(input("higher "))
except ValueError:
    print("Type integers only please")





