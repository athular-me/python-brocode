import random
import string
chars=string.ascii_letters+string.digits+string.punctuation +" "
print(chars)
is_running=True
messages=[]
encryptedmessages=""
decryptedmessages=""
def shuffle():
    global chars1
    chars1=list(chars)
    random.shuffle(chars1)
    pass

def userinput():
    global usermessage
    usermessage=input("enter message : ")
    if usermessage.strip()=="":
            usermessage=input("Input is invalid.\nEnter message : ")

    pass
def encrypt():
    global chars1
    global encryptedmessages
    for i in usermessage:
         index1=chars.index(i)
         element1=chars1[index1]
         encryptedmessages+=element1
    print(f"encrypted message : {encryptedmessages}")    
    pass
def decrypt():
    global encryptedmessages
    global decryptedmessages
    for j in encryptedmessages:
         index2=chars1.index(j)
         element2=chars[index2]
         decryptedmessages+=element2
    print(f"decrypted message : {decryptedmessages}")
    pass
def game_exit():
     global is_running
     is_running=False
     pass


def main():
    global encryptedmessages
    global decryptedmessages
    while is_running:
        user=input("1. Type message\n2.Encrypt message\n3.Decrypt message\n4.Try\n5.Exit\n")
        if user=='1':
             userinput()
             pass
        elif user=='2':
             encrypt()
             encryptedmessages=""
             decryptedmessages=""
             pass
        elif user=='3':
             decrypt()
        elif user=='4':
          shuffle()
          userinput()
        elif user=='5':
          game_exit()
        else:
             print("invalid input...\nexiting...")
        pass
    
print()
print()
if __name__=="__main__":
    main()
