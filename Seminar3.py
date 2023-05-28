##Alex Olhovskiy

import random as rand
import math
import timeit


##18
##print("Enter list size")
##N=int(input())
##arr=[int(a) for a in input().split(',')]
##print("Enter X")
##X=int(input())
###arr=[rand.randint(1,10) for i in range(N)]
###print(N)
##print(arr)
##print(X)

code_to_test = """
import random as rand
arr=[rand.randint(1,10) for i in range(1000)]
X=5
arr2=[abs(i-X) for i in arr]
print(arr2)
print(f'->{arr[arr2.index(min(arr2))]}')
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


code_to_test = """
import random as rand
arr=[rand.randint(1,10) for i in range(1000)]
X=5
arr.sort()
res=0
i=0
print(len(arr))
while i<len(arr) and arr[i]<X:
    i+=1

if i==len(arr):
    res=arr[len(arr)-1]
elif arr[i]==X:
    res=arr[i]
else:
    if i==0:
        res=arr[i]  
    else:
        if arr[i]-X<X-arr[i-1]:
            res=arr[i]
        else:
            res=arr[i-1]


print(f"->{res}")
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
