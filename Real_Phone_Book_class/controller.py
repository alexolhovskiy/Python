##Alex Olhovskiy
import source
import user_interface as uint

my_interface=uint.Interface()
my_source=source.Module()

def MyProg():
    enter=0
    while enter!=8:
        enter=my_interface.MyMenu()
        if enter==1:
            my_source.Load()
        elif enter==2:
            my_source.Save()
        elif enter==3:
            arr=my_source.Search(my_interface.Search())
            for i in arr:
                my_interface.Print(i)
        elif enter==4:
            my_source.Edit(my_interface.Edit())
        elif enter==5:
            my_source.Delete(my_interface.Delete())
        elif enter==6:
            my_source.Add(my_interface.Add())
        elif enter==7:
            arr=my_source.Print()
            ##print(arr)
            for i in arr:
                my_interface.Print(i)
        else:
            pass
