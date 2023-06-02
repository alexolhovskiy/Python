##Alex Olhovskiy

##26
print("Enter A")
a=int(input())

print("Enter B")
b=int(input())

def MyPow(a,b):
    if b>0:
        b-=1
        a*=MyPow(a,b)
    else:
        return 1
    return a

print(MyPow(a,b))

##28
print("Enter A")
a=int(input())

print("Enter B")
b=int(input())

def MySum(a,b):
    if b>0:
        b-=1
    else:
        return a
    return 1+MySum(a,b)

print(MySum(a,b))
