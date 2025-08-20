kart={"popcorn":1,
      "hot dog":2,
      "giant pretzel":2,
      "asst candy":1,
      "soda":1,
      "bottled water":1}
userinput=input("do you want to continue - y/n : ").strip().lower()
fooditems=[]
quantities=[]
sectionalprices=[]
totalprice=0
while userinput=='y':
    food=input("enter food item name : ").strip().lower()
    quantity=int(input(f"enter the quantity of {food}/s : "))
    while food=="" or quantity<0 or kart.get(food)==None:
        print("invalid inputs")
        food=input("enter food item name : ").strip().lower()
        quantity=int(input(f"enter the quantity of {food}/s : "))
    fooditems.append(food)
    quantities.append(quantity)
    sectionalprice=kart.get(food)*quantity
    sectionalprices.append(sectionalprice)
    userinput=input("do you want to continue - y/n : ").strip().lower()
print('-------------------------')
for i in fooditems:
    print(i,end=" ")
print()
for j in quantities:
    print(j,end=" ")
print()
for k in sectionalprices:
    totalprice+=k
    print(k,end=" ")
print()
print(totalprice)