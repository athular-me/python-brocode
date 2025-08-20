import time 
mytime=int(input("enter time in seconds : "))
for second in range(mytime,0,-1):
    seconds=second%60
    minutes=int(second/60)%60
    hour=int(second/3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(2)
print("time is up .....!")