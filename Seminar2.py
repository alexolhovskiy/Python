import random as rand
import math

#Coins(#10)

def CoinsScattering():
    print("Enter coins number")
    num=int(input())
    arr=[]
    for i in range(num):
        if rand.random()>=0.5:
            arr.append(1)  
        else:
            arr.append(0)
    print(arr)
    return arr


def Coins(arr):
    coat=0
    shrill=0
    for n in arr:
        if n>0:
            coat+=1
        else:
            shrill+=1

    if coat>shrill:
        print("{} coins with shrill".format(shrill))
    else:
        print("{} coins with coat".format(coat))
        
Coins(CoinsScattering())


#Two numbers(#12)

def TwoNumbers():
    arr=[]
    arr.append(rand.randint(0,1001))
    arr.append(rand.randint(0,1001))
    arr.append(arr[0]+arr[1])
    arr.append(arr[0]*arr[1])
    print(arr)
    return arr


def NumFind(S,P):
    Arr=[]
    D=S**2-4*P
    if D>=0:
        y1=(S+math.sqrt(D))/2
        y2=(S-math.sqrt(D))/2
        if y1>=0 and y1<=1000:
            print(y1)
            Arr.append(y1)
        else:
            print(y2)
            Arr.append(y2)
    Arr.append(S-Arr[0])
    print(Arr)
    return Arr


def ListComparison(arr,Arr):
    if (arr[0]==Arr[0] or arr[0]==Arr[1])and(arr[1]==Arr[0] or arr[1]==Arr[1]):
        print("Yes")
    else:
        print("No")


arr=TwoNumbers()
ListComparison(arr,NumFind(arr[2],arr[3]))


#Pow(#14)

def TwoPow():
    print("Enter number")
    num=int(input())
    res=2
    i=0
    while res<num:
        res=2
        res**=i
        i+=1
        if res<num:
            print(res,end=' ')

TwoPow()
