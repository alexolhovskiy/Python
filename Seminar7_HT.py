##Alex Olhovskiy

##34

#frase="пара-ра-рам рам-пам-папам па-ра-па-дам"
frase=input("Enter your frase")
print(frase)
letter=['а','я','ы','у','е','и','о','ю','э']
arr=frase.split(' ')

def func(arr):
    count=calc(arr[0])
    for i in arr[1:]:
        if count!=calc(i):
            return "Пам парам"
    return "Парам пам-пам"
        
def calc(word):
    cnt=0
    for i in word:
        if letter.count(i)>0:
            cnt+=1
    return cnt

print(func(arr))


##36

def print_operation_table(func,num_rows=6,num_columns=6):
    for i in range(1,num_rows+1):
        for j in range(1,num_columns+1):
            print(func(i,j),end='\t')
        print('\n')
        
num_rows=int(input("Enter num of rows"))
num_columns=int(input("Enter num of columns"))

print_operation_table(lambda x, y: x * y, num_rows, num_columns)



