unit1=input("enter source unit (K/C/F) : ").lower()
unit11=float(input(f'enter howmany {unit1}/s : '))
unit2=input("enter destination unit (K/C/F) : ").lower()
result=0
if unit1=='k':
    if unit2=="k":
        result=unit11
    elif unit2 =='c':
        result=unit11 - 273.15
    elif unit2=='f':
        result=(unit11 - 273.15) * (5/9) + 32
    else:
        print('invalid inputs.')
elif unit1=="c":
    if unit2=='c':
        result=unit11
    elif unit2=='k':
        result=unit11+273.15
    elif unit2=='f':
        result=(unit11 * 59) + 32
    else:
        print("invalid inputs.")
elif unit1=="f":
    if unit2=='c':
        result=(unit11 - 32) * 95
    elif unit2=='k':
        result=(unit11 - 32)*( 9/5)+273.15
    elif unit2=='f':
        result=unit11
    else:
        print('invalid input')
print(f"{unit11} {unit1} : {result} {unit2}")