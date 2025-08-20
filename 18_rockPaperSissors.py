#rock paper scissors game 
import random
options=("rock","paper","scissors")
my_score=0
computer_score=0
rounds=5
while rounds>0:
    computer=random.choice(options)
    guess=input("choice : ").strip().lower()
    print(f"computer:{computer}")
    print(f"guess:{guess}")
    if computer=="rock":
        if guess=="paper":
            my_score+=1
        elif guess=="scissors":
            computer_score+=1
        print(f"my score is {my_score}")
        print(f"computer score is {computer_score}")
    elif computer=="paper":
        if guess=="rock":
            computer_score+=1
        elif guess=="scissors":
            my_score+=1
        print(f"my score is {my_score}")
        print(f"computer score is {computer_score}")


    elif computer=="scissors":
        if guess=="rock":
            my_score+=1
        elif guess=="paper":
            computer_score+=1
        print(f"my score is {my_score}")
        print(f"computer score is {computer_score}")


    else:
        print("invalid inputs")
    rounds-=1
if my_score>computer_score:
    print("you win")
elif my_score<computer_score:
    print("you lose")
else:
    print("less go for tie breaker...")
    