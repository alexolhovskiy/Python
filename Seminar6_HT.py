##Alex Olhovskiy

import random as rand
import math

##30
print("Enter start")
start=int(input())
print("Enter difference")
dif=int(input())
print("Enter length")
length=int(input())

arr=[]

for i in range(length):
    arr.append(start+dif*i)

print(arr)


##32

print("Enter list length")
length=int(input())
print("Enter min range")
minr=int(input())
print("Enter max range")
maxr=int(input())
dif=maxr-minr

arr=[rand.randint(minr-dif,maxr+dif)for i in range(length)]

print(arr)

arr1=[]
for i in range(len(arr)):
    if arr[i]>minr and arr[i]<maxr:
       arr1.append(i)
       
print(arr1)
