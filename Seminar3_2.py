##Alex Olhovskiy
import random as rand
import math

##16
print("Enter list size")
N=int(input())

print("Enter X")
X=int(input())

arr=[rand.randint(1,10) for i in range(N)]
print(N)
print(arr)
print(X)
print(f"->{arr.count(X)}")


##18
##В файле Seminar3.py представлен более классический вариан решения
##более муторный, но, однако, в 5 раз быстрее по выполнению
print("Enter list size")
N=int(input())

print("Enter X")
X=int(input())

arr=[rand.randint(1,10) for i in range(N)]
print(N)
print(arr)
print(X)

arr2=[abs(i-X) for i in arr]
print(f'->{arr[arr2.index(min(arr2))]}')



##20
d_arr=[{1:'aeioulnstr',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'},
       {1:'авеинорст',2:'дклмпу',3:'бгёья',4:'йы',5:'жзхцч',8:'шэю',10:'фщъ'}]

print("Enter your word")
my_word=input()

ind=0
flag=my_word.encode('utf-8')
if flag[0]>=97 and flag[0]<=122:
    ind=0
    print("english")
else:
    ind=1
    print("русский")

res=0
for i in my_word:
    for key,val in d_arr[ind].items():
        if val.find(i)>=0:
             res+=key

print(res)
