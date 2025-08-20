source=input("from where to : (kg / pounds ) ")
kilogram=0
pounds=0
if source=='kg':
    kilogram=float(input("how many kilograms need to be converted : "))
    pounds=kilogram * 2.20462
    print(f"{kilogram} Kgs = {pounds} lbs")
elif source=='pounds':
    pounds=float(input("how many pounds need to be converted : "))
    kilogram = pounds * 0.453592
    print(f"{pounds} lbs = {kilogram} kgs")

else:
    print("invalid input .")