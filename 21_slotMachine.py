import random
import time
symbols = ['🍒', '🍋', '🍉', '🍇', '🍊', '⭐', '🔔', '💎', '🍀']
is_playing=True
chances=10
total_score=0
def deposite():
    global total_score
    cash=int(input("enter the deposite : "))
    total_score+=cash
    pass

def check_score():
    global total_score
    points=0
    if slot[0]==slot[1]==slot[2]:
        points+=100
    elif slot[0]==slot[1] or slot[2]==slot[1] or slot[0]==slot[2]:
        points+=50
    else:
        points-=20 
    total_score=total_score+points
    pass
def spin():
    global slot
    global chances
    slot=[]
    for j in range(3):
        time.sleep(0.5)
        print('.',end="",flush=True)
    print()
    for i in range(3):
        symbol=random.choice(symbols)
        slot.append(symbol)
    print(slot)
    check_score()
    chances-=1
    pass
def score():
    print(f"your balance : {total_score}")
    pass
def check():
    if total_score<=0 :
        print(f"you have no balance available.\ndeposit cash.\nAvailable balance:{total_score}")
        deposite()
    elif chances==0:
        print(f"You are out of chances.\nPlease restart the game.\nYour withdraw money is {total_score}.\nHope you enjoy playing...")
        game_exit()
    pass
def game_exit():
    global is_playing
    is_playing=False

def main():
    while is_playing:
        print("------------------------------")
        print(f"1.deposite cash\n2.spin\n3.balance check\n4.exit")
        userinput=input("choice: ")
        if userinput=='1':
            deposite()
        elif userinput=='2':
            check()
            if is_playing:
                spin()
        elif userinput=='3':
            print(f"balance:{total_score}")
        elif userinput=='4':
            game_exit()
        else:
            print("invalid input\n")
        pass
if __name__=="__main__":
    main()
    pass