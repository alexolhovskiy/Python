##Alex Olhovskiy
import json

phone_book=[]

def Add(my_arr):
    person={}
    person['name']=my_arr[0]
    person['comment']=my_arr[1]
    person['phones']=my_arr[2]
    phone_book.append(person)
    
def Save():
    with open('file.txt','w') as file:
        for person in phone_book:
            file.write(f'{json.dumps(person)}\n')

def Load():
    phone_book.clear()
    with open('file.txt','r') as file:
        for line in file:
            phone_book.append(json.loads(line))


def Search(word):
    arr=[]
    for person in phone_book:
        temp=[]
        temp.append(person['name'])
        temp.append(person['comment'])
        temp.extend(person['phones'])
        my_str=' '.join(temp).lower()
        if my_str.count(word.lower())>0:
            t=(phone_book.index(person),person)
            arr.append(t)
    return arr


def Delete(ind):
    if ind>0:
        phone_book.pop(ind)


def Edit(my_tuple):
    ind=my_tuple[0]
    arr=my_tuple[1]
    if arr[0]!='':
        phone_book[ind]['name']=arr[0]
    if arr[1]!='':
        phone_book[ind]['comment']=arr[1]
    if len(arr[2])>0:
        phone_book[ind]['phones'].append(arr[2])

        
def Print():
    arr=[]
    for person in phone_book:
        t=(phone_book.index(person),person)
        arr.append(t)
    return arr
