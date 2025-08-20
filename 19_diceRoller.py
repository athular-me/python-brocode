import random
import time
dice_art = {
    1: (
        "┌─────┐\n"
        "│     │\n"
        "│  ●  │\n"
        "│     │\n"
        "└─────┘"
    ),
    2: (
        "┌─────┐\n"
        "│ ●   │\n"
        "│     │\n"
        "│   ● │\n"
        "└─────┘"
    ),
    3: (
        "┌─────┐\n"
        "│ ●   │\n"
        "│  ●  │\n"
        "│   ● │\n"
        "└─────┘"
    ),
    4: (
        "┌─────┐\n"
        "│ ● ● │\n"
        "│     │\n"
        "│ ● ● │\n"
        "└─────┘"
    ),
    5: (
        "┌─────┐\n"
        "│ ● ● │\n"
        "│  ●  │\n"
        "│ ● ● │\n"
        "└─────┘"
    ),
    6: (
        "┌─────┐\n"
        "│ ● ● │\n"
        "│ ● ● │\n"
        "│ ● ● │\n"
        "└─────┘"
    )
}

my_score=0
computer_score=0
is_playing =True
while is_playing:
    computer=random.choice(list(dice_art.keys()))
    my_guess=random.choice(list(dice_art.keys()))
    print('-----computer-----')
    print("computer is rolling...")
    time.sleep(2)
    print(dice_art.get(computer))
    print('-----my guess-----')
    print("you are rolling...")
    time.sleep(2)
    print(dice_art.get(my_guess))
    if computer>my_guess:
        computer_score+=1
    elif my_guess>computer:
        my_score+=1
    user=input("do you want to continue-(y/n) : ").lower().strip()
    if not user =='y':
        is_playing=False
print('------------------------')
print(f"your score is {my_score}.\nComputer score is {computer_score}.")
if computer_score>my_score:
    print("you lose...")
else:
    print("you win...")