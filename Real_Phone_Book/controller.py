##Alex Olhovskiy
import source
import user_interface as uint

def MyProg():
    enter=0
    while enter!=8:
        enter=uint.MyMenu()
        if enter==1:
            source.Load()
        elif enter==2:
            source.Save()
        elif enter==3:
            arr=source.Search(uint.Search())
            for i in arr:
                uint.Print(i)
        elif enter==4:
            source.Edit(uint.Edit())
        elif enter==5:
            source.Delete(uint.Delete())
        elif enter==6:
            source.Add(uint.Add())
        elif enter==7:
            arr=source.Print()
            ##print(arr)
            for i in arr:
                uint.Print(i)
        else:
            pass
