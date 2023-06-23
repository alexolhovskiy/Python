##Alex Olhovskiy
import resource as res

def Print(item):
    print(item[0],item[1]['name'],item[1]['comment'],
          ' '.join(item[1]['phones']),sep=' ')


def Add():
    person=[]
    person.append(input(res.e_name))
    person.append(input(res.e_com))
    temp=[]
    while input(res.a_phone)!='n':
        temp.append(input(res.e_phone)) 
    person.append(temp)
    print(person)
    return person


def Delete():
    ind=int(input(res.e_ind))
    if input(res.Del(ind))=='y':
        return ind
    else:
        return -1

def Edit():
    ind=int(input(res.e_ind))
    person=[]
    if input(res.Change_name(ind))=='y':
                person.append(input(res.e_name))
    else:
        person.append("")
    if input(res.Change_comm(ind))=='y':
        person.append(input(res.e_com))
    else:
        person.append("")
    if input(res.Change_phones(ind))=='y':
        temp=[]
        while input(res.a_phone)!='n':
            temp.append(input(res.e_phone))
        person.append(temp)
    else:
        person.append("")
    return ind,person

def Search():
    return input(res.e_any)

def MyMenu():
    print('-'*100)
    print(res.menu_s)
    for v in res.menu:
        print(v,end='\n')
    enter=int(input(res.e_choise))
    print('-'*100)
    return enter

