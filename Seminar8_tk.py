##Alex Olhovskiy
from tkinter import *
from tkinter import ttk
import random as rand

import json
 
root = Tk()
root.title("MyList")
root.geometry("400x400")
root.columnconfigure(index=0,weight=1)
root.columnconfigure(index=1,weight=4)

for n in range(13):
    root.rowconfigure(index=n,weight=1)


label=ttk.Label(text='Имя',anchor=W,background="#FFCDD2",
                width=22)
label.grid(column=0,row=0,sticky=NS)
entry = ttk.Entry()
entry.grid(column=0,row=1,padx=6,pady=6,sticky=EW)

label1=ttk.Label(text='Комментарий',anchor=W,background="#FFCDD2",
                width=22)
label1.grid(column=0,row=2,sticky=NS)
entry1 = ttk.Entry()
entry1.grid(column=0,row=3,padx=6,pady=6,sticky=EW)

label2=ttk.Label(text='Телефон',anchor=W,background="#FFCDD2",
                width=22)
label2.grid(column=0,row=4,sticky=NS)
entry2 = ttk.Entry()
entry2.grid(column=0,row=5,padx=6,pady=6,sticky=EW)



phone_book=[]


def Add():
    person={}

    person['name']=entry.get()
    person['comment']=entry1.get()
    person['phones']=entry2.get().split()
    
    phone_book.append(person)
    Print()



def Save():
    with open('file.txt','w') as file:
        for person in phone_book:
            file.write(f'{json.dumps(person)}\n')

def Load():
    phone_book.clear()
    with open('file.txt','r') as f:
        for line in f:
            phone_book.append(json.loads(line))
    
arr_search=[]
def Search():
    name=entry.get().lower()
    comment=entry1.get().lower()
    phones=entry2.get().lower()
    lb.delete(0,END)
    arr_search.clear()
    my_str=''
    for p in phone_book:
        p_name=p['name'].lower()
        p_comment=p['comment'].lower()
        p_phones=' '.join(p['phones']).lower()
        if name!='' and p_name.count(name)>0:
            lb.insert(END,f"{phone_book.index(p)} {p['name']} {p['comment']} {' '.join(p['phones'])}")
            arr_search.append(phone_book.index(p))
        if comment!='' and p_comment.count(comment)>0:
            lb.insert(END,f"{phone_book.index(p)} {p['name']} {p['comment']} {' '.join(p['phones'])}")
            arr_search.append(phone_book.index(p))
        if phones!='' and p_phones.count(phones)>0:
            lb.insert(END,f"{phone_book.index(p)} {p['name']} {p['comment']} {' '.join(p['phones'])}")
            arr_search.append(phone_book.index(p))

def Delete():
    i=lb.curselection()
    phone_book.pop(phone_book.index(phone_book[i[0]]))
    Print()


def Edit():
    global current_selected
    print(current_selected[0])
    if len(arr_search)>0:
        phone_book[arr_search[current_selected[0]]]['name']=entry.get()
        phone_book[arr_search[current_selected[0]]]['comment']=entry1.get()
        phone_book[arr_search[current_selected[0]]]['phones']=entry2.get().split()
    else:
        phone_book[current_selected[0]]['name']=entry.get()
        phone_book[current_selected[0]]['comment']=entry1.get()
        phone_book[current_selected[0]]['phones']=entry2.get().split()
    Print()


def Print():
    arr_search.clear()
    lb.delete(0,END)
    for i in phone_book:
        lb.insert(END,f"{phone_book.index(i)} {i['name']} {i['comment']} {' '.join(i['phones'])}")

current_selected=0
       
def Get():
    global current_selected
    current_selected=lb.curselection()
    entry.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    if len(arr_search)>0:
        entry.insert(0,phone_book[arr_search[current_selected[0]]]['name'])
        entry1.insert(0,phone_book[arr_search[current_selected[0]]]['comment'])
        entry2.insert(0,' '.join(phone_book[arr_search[current_selected[0]]]['phones']))
    else:
        entry.insert(0,phone_book[current_selected[0]]['name'])
        entry1.insert(0,phone_book[current_selected[0]]['comment'])
        entry2.insert(0,' '.join(phone_book[current_selected[0]]['phones']))


button=ttk.Button(text="Получить",command=Get)
button.grid(column=0,row=6,padx=0,pady=0,sticky=NSEW)        
button1=ttk.Button(text="Загузить",command=Load)
button1.grid(column=0,row=7,padx=0,pady=0,sticky=NSEW)
button2=ttk.Button(text="Сохранить",command=Save)
button2.grid(column=0,row=8,padx=0,pady=0,sticky=NSEW)
button3=ttk.Button(text="Найти",command=Search)
button3.grid(column=0,row=9,padx=0,pady=0,sticky=NSEW)
button4=ttk.Button(text="Редактировать",command=Edit)
button4.grid(column=0,row=10,padx=0,pady=0,sticky=NSEW)
button5=ttk.Button(text="Удалить",command=Delete)
button5.grid(column=0,row=11,padx=0,pady=0,sticky=NSEW)
button6=ttk.Button(text="Добавить",command=Add)
button6.grid(column=0,row=12,padx=0,pady=0,sticky=NSEW)
button7=ttk.Button(text="Показать",command=Print)
button7.grid(column=0,row=13,padx=0,pady=0,sticky=NSEW)


 
# создаем список
lb=Listbox()
lb.grid(row=0,rowspan=14,column=1,sticky=NSEW,
        padx=5,pady=5)

scroll=ttk.Scrollbar(orient="vertical",command=lb.yview)
scroll.grid(column=2,row=0,rowspan=14,sticky=NS)
lb["yscrollcommand"]=scroll.set


root.mainloop()
