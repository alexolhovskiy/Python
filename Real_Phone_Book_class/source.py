##Alex Olhovskiy
import json


class Module:
    
    def __init__(self):
        self.phone_book=[]

    

    def Add(self,my_arr):
        person={}
        person['name']=my_arr[0]
        person['comment']=my_arr[1]
        person['phones']=my_arr[2]
        self.phone_book.append(person)
        
    def Save(self):
        with open('file.txt','w') as file:
            for person in self.phone_book:
                file.write(f'{json.dumps(person)}\n')

    def Load(self):
        self.phone_book.clear()
        with open('file.txt','r') as file:
            for line in file:
                self.phone_book.append(json.loads(line))


    def Search(self,word):
        arr=[]
        for person in self.phone_book:
            temp=[]
            temp.append(person['name'])
            temp.append(person['comment'])
            temp.extend(person['phones'])
            my_str=' '.join(temp).lower()
            if my_str.count(word.lower())>0:
                t=(self.phone_book.index(person),person)
                arr.append(t)
        return arr


    def Delete(self,ind):
        if ind>0:
            self.phone_book.pop(ind)


    def Edit(self,my_tuple):
        ind=my_tuple[0]
        arr=my_tuple[1]
        if arr[0]!='':
            self.phone_book[ind]['name']=arr[0]
        if arr[1]!='':
            self.phone_book[ind]['comment']=arr[1]
        if len(arr[2])>0:
            self.phone_book[ind]['phones'].clear()
            self.phone_book[ind]['phones'].extend(arr[2])

            
    def Print(self):
        arr=[]
        for person in self.phone_book:
            t=(self.phone_book.index(person),person)
            arr.append(t)
        return arr
