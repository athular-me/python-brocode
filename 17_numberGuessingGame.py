import random
low=int(input("low value : "))
high=int(input("high value : "))
computer=random.randint(low,high)
guess=3
while guess>0:
    myguess=int(input("enter the number : "))
    if myguess>computer:
        print("your guess is high...")
        guess-=1
    elif myguess<computer:
        print("your guess is low...")
        guess-=1
    else:
        print("you guessed correct")
        break
