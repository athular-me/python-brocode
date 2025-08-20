operator=input("enter operator : ")
num1=float(input("enter number1 : "))
num2=float(input("enter number2 : "))
result=0
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='*':
    result=num1*num2
elif operator=='/':
    result=num1/num2
else:
    print(f"invalid operator .")
print(result)