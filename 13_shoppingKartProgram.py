#shopping kart program
foods=[]
quantities=[]
prices=[]
totalprice=0
userinput=input("do you want to continue - (y/n) :").lower()

while userinput=='y':
    food=input("whats the food item : ").strip()
    price=float(input("what its price : "))
    quantity=int(input(f"enter the quantity of fooditem {food} : "))
    while food=="" or price<=0:
            food=input("whats the food item : ").strip()
            price=float(input("what its price : "))
            quantity=int(input(f"enter the quantity of fooditem {food} : "))

    foods.append(food)
    prices.append(price)
    quantities.append(quantity)
    userinput=input("do you want to continue - (y/n) :").lower()
for i in range(len(quantities)):
    totalprice+=quantities[i] * prices[i]
print('-------------------------------')
for food in foods:
     print(f"{food:<10}",end=" ")
print()
for quantity in quantities:
     print(f"{quantity:<10}",end=" ")
print()
for price in prices:
     print(f"{price:<10}",end=" ")
print()
print('-------------------------------')
print(totalprice)
print('-------------------------------')
