#shopping kart program -item ,quantity , price

itemname=input("enter item name :")
quantity=int(input(f"enter the quantity of {itemname} purchased : "))
price=float(input(f"enter the price of {itemname} : "))
totalPrice=quantity*price
print(f"total cash to pay for {itemname} is {totalPrice}")