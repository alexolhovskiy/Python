##Alex Olhovskiy

import random as rand

##22
print("Enter size of first set")
n=int(input())
print("Enter size of second set")
m=int(input())

def SetSet(k):
    my_set=set()
    for i in range(k):
        ##my_set.add(rand.randint(0,10))
        print("Enter next element")
        my_set.add(int(input()))
    return my_set

print("Set first set")
set_1=SetSet(n)
print("Set second set")
set_2=SetSet(m)

arr=list(set_1.intersection(set_2))
arr.sort()

print(n)
print(m)
print(set_1)
print(set_2)
print(arr)


##24
print("Enter number of beds")
n=int(input())

print("Enter number of bushes per bed")
m=int(input())

arr=[[rand.randint(0,10) for j in range(m)]for i in range(n)]

print(arr)

e_sum=0
e_max=0
for i in arr:
    for j in range(len(i)):
        if j==(len(i)-2):
            e_sum=sum(i[j:])+i[0]
            if e_sum>e_max:
                e_max=e_sum
        elif j==(len(i)-1):
            e_sum=sum(i[0:2])+i[len(i)-1]
            if e_sum>e_max:
                e_max=e_sum
        else:
            e_sum=sum(i[j:j+3])
            if e_sum>e_max:
                e_max=e_sum
               
print(e_max)
        
