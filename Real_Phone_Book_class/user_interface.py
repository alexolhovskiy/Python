##Alex Olhovskiy
import resource as res

my_r=res.Text()
class Interface:

##    def __init__(self):
##        self.my_r=res.Text()

    def Print(self,item):
        print(item[0],item[1]['name'],item[1]['comment'],
              ' '.join(item[1]['phones']),sep=' ')


    def Add(self):
        person=[]
        person.append(input(my_r.e_name))
        person.append(input(my_r.e_com))
        temp=[]
        while input(my_r.a_phone)!='n':
            temp.append(input(my_r.e_phone)) 
        person.append(temp)
        print(person)
        return person


    def Delete(self):
        ind=int(input(my_r.e_ind))
        if input(my_r.Del(ind))=='y':
            return ind
        else:
            return -1

    def Edit(self):
        ind=int(input(my_r.e_ind))
        person=[]
        if input(my_r.Change_name(ind))=='y':
                    person.append(input(my_r.e_name))
        else:
            person.append("")
        if input(my_r.Change_comm(ind))=='y':
            person.append(input(my_r.e_com))
        else:
            person.append("")
        if input(my_r.Change_phones(ind))=='y':
            temp=[]
            while input(my_r.a_phone)!='n':
                temp.append(input(my_r.e_phone))
            person.append(temp)
        else:
            person.append("")
        return ind,person

    def Search(self):
        return input(my_r.e_any)

    def MyMenu(self):
        print('-'*100)
        print(my_r.menu_s)
        for v in my_r.menu:
            print(v,end='\n')
        enter=int(input(my_r.e_choise))
        print('-'*100)
        return enter

