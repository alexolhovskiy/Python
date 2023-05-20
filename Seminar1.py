#Alex Olhovskiy

import math

##1.three-digit number sum(#2)

##1.0#############################    
def SumNum(num_int):
    sum=0
    for i in range(0,3):
        sum+=num_int%10
        num_int//=10
        print(sum,num_int, sep="*")
    return sum

##1.1#############################
def SumNum2(num_str):
    sum=0
    for i in num_str:
        sum+=int(i)
    return sum

#################################

def ThreeDigNum():
    m=input("Enter three-digit number")
    n=int(m)
    if n>99 and n<1000:
        print(f"Sum is: {SumNum2(m)}",end='\n\n')
        print(f"Sum is: {SumNum(n)}",end='\n\n')
    else:
        print("You enter wrong number! Check it!",end='\n\n')


ThreeDigNum()

##2.Cranes(#4)

def Cranes():
    m=int(input("Enter whole number of cranes"))
    if m%6==0:
        peter=m/6
        kate=2*m/3
        serg=m/6
        print(f"Peter made {int(peter)} cranes, Kate made {int(kate)} crans, Serg made {int(serg)} crans",end='\n\n')
    else:
        print("Your number not compatible with this task",end='\n\n')


Cranes()

##3.Lucky ticket(#6)

def LuckyTick():
    m=input("Enter ticket number")
    if len(m)==6:
        first_part=int(m)//1000
        second_part=int(m)%1000
        if SumNum(first_part)==SumNum(second_part):
            print("This is lacky ticket!",end='\n\n')
        else:
            print("Good luck next time!",end='\n\n')
    else:
        print("You have wrong ticket!",end='\n\n')

LuckyTick()

##4.Chocolate bar(#8)

def ChocoBar():
    row=int(input("Enter chocolate bar rows"))
    column=int(input("Enter chocolate bar columns"))
    k=int(input("Enter piece size"))
    if k%row==0 or k%column==0:
        if k<(row*column):
            print("Possible!",end='\n\n')
        elif k==(row*column):
            print("You want whole bar!",end='\n\n')
        else:
            print("You want more than now is!",end='\n\n')
    else:
        print("Impossible!",end='\n\n')
    
ChocoBar()
