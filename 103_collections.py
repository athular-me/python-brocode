#lists []

fruits=["apple","melon","pineapple","cherry"]
fruits.append("orange")

fruits.remove("apple")
print(len(fruits))
fruits.insert(0,"jackfruit")
print("cherry" in fruits)
fruits[0]="dragon fruit" #mutable or changable ,also ordered .
print(fruits)

#sets

fruits={"apple","melon","pineapple","cherry"}
fruits.add("jack fruit")
fruits.remove("melon")
fruits.pop()
print(fruits)

#tuple

fruits=("apple","melon","pineapple","cherry")
print(dir(fruits))
print(fruits.count("melon"))
print(fruits.index("melon"))

#dictionary

demo={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
print(demo.get('g'))
print(demo.get('a'))
demo.update({'g':7})
print(demo)
for key,value in demo.items():
    print(f"{key}:{value}",end=" | ")

