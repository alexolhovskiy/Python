##Alex Olhovskiy
import json

menu={'1':'Загрузить - нажмите 1',
      '2':'Сохронить - нажмите 2',
      '3':'Найти - нажмите 3',
      '4':'Редактировать - нажмите 4',
      '5':'Удалить - нажмите 5',
      '6':'Добавить - нажмите 6',
      '7':'Показать - нажмите 7',
      '8':'Уйти - нажмите 8'}

    
def MyMenu():
    print('Menu')
    for v in menu.values():
        print(v,end='\n')

phone_book=[]

def Add():
    person={}

    person['name']=input('Введите имя')
    person['comment']=input('Введите комментарий')
    person['phones']=[]
    while input('Добавить номер телефона? y/n')!='n':
        person['phones'].append(input('Введите номер телефона'))
    phone_book.append(person)



def Save():
    with open('file.txt','w') as file:
        for person in phone_book:
            file.write(f'{json.dumps(person)}\n')

def Load():
    phone_book.clear()
    with open('file.txt','r') as f:
        for line in f:
            phone_book.append(json.loads(line))

def Print():
    for i in phone_book:
        print(i['name'],i['comment'],' '.join(i['phones']),sep=' ')


def Search():
    word=input('Введите что хотите найти')
    arr=[]
    for person in phone_book:
        temp=[]
        temp.append(person['name'])
        temp.append(person['comment'])
        temp.extend(person['phones'])
        my_str=' '.join(temp).lower()
        if my_str.count(word.lower())>0:
            print(phone_book.index(person),end='\n')
            print(person['name'],person['comment'],
                  ' '.join(person['phones']),sep=' ')
        


def Delete():
    ind=int(input('Введите индекс контакта'))
    if input(f'Вы точно хотите удалить контакт {ind} y/n')=='y':
        phone_book.pop(ind)


def Edit():
    ind=int(input('Введите индекс контакта'))
    if input(f'Вы точно хотите изменить имя контакта {ind} y/n')=='y':
        phone_book[ind]['name']=input("Введите новое имя")
    elif input(f'Вы точно хотите изменить комментарий к контакту {ind} y/n')=='y':
        phone_book[ind]['comment']=input("Введите новый комментарий")
    elif input(f'Вы точно хотите изменить номера телефонов контакта {ind} y/n')=='y':
        phone_book[ind]['phones'].clear()
        while input('Добавить номер телефона? y/n')!='n':
            phone_book[ind]['phones'].append(input('Введите номер телефона'))
    else:
        return



def MyProg():
    enter=0
    while enter!=8:
        print('-'*100)
        MyMenu()
        enter=int(input('Делайте выбор'))
        print('-'*100)
        if enter==1:
            Load()
        elif enter==2:
            Save()
        elif enter==3:
            Search()
        elif enter==4:
            Edit()
        elif enter==5:
            Delete()
        elif enter==6:
            Add()
        elif enter==7:
            Print()
        else:
            pass

MyProg()                    
