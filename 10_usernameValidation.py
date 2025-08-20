username=input("enter username : ")
if len(username) <=12 and username.count(" ")==0 and username.isalpha():
    print("valid username.")
else:
    print("invalid username.")