balance=0
is_running=True
def show_balance():
    print(f"Balance : {balance}")
def deposite():
    global balance
    sum=float(input("sum : "))
    balance+=sum
def withdraw():
    global balance
    sum=float(input("sum : "))
    if sum>balance:
        print(f"Not enough funds available...\nAvailable banance : {balance}")
    else:
        balance-=sum
# def check():
#     if balance<0:
#         print(f"Not enough funds available...\nAvailable banance : {balance}")
#         exit()
def exit():
    global is_running
    is_running=False
    print('exiting...')
    return is_running
def main():
    while is_running:
        print('-----Bank-----')
        print('1.show balance\n2.deposite\n3.withdraw\n4.exit')
        userinput=input("enter preference(from 1-4) : ")
        match userinput:
            case '1':
                show_balance()
                # check()
            case '2':
                deposite()
            case '3':
                withdraw()
                # check()
            case '4':
                exit()
            case _:
                print(f"{userinput} is an invalid input...")
                userinput=input("enter preference(from 1-4) : ")

if __name__=="__main__":
    main()