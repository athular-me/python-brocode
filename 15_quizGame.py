questions=("1.whats the color of sky?","2.how many tires do normal bicycles have ? ","3.color of indian hair ? ")
options=(("1.Blue\n2.black\n3.yellow"),("1.1\n2.2\n3.3"),("1.Blue\n2.black\n3.yellow"))
answers=[]
correctanswers=(1,2,2)
totalscore=0
questionnumber=0
while True:
    print(questions[questionnumber])
    print(options[questionnumber])
    answer=int(input("enter correct answer in integer : "))
    answers.append(answer)
    if answer==correctanswers[questionnumber]:
        totalscore+=1
    questionnumber+=1
    if questionnumber>=len(questions):
        break

print('--------------------------')
for answer in answers:
    print(answer,end=" ")
print()
for correctanswer in correctanswers:
    print(correctanswer,end=" ")
print()
print(totalscore)