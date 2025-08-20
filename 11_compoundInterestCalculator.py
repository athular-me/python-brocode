
while True:
    userinput=input("enter 'n' to exit : ").lower()
    if userinput=='n':
        print("exiting...")
        break
    elif userinput=='y':
        p=float(input("enter principal amount : "))
        r=float(input("enter interest rate : "))
        y=int(input("enter years to be invested : "))
        ci=p * (pow(1 + (r/100),y))
        i=ci-p
        print(f"compound interest for amount {p} for {y} years for interest rate {r} is {i}")
    else:
        print("invalid ...")

        
