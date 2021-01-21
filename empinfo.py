class Employee:
    def __init__(self,empid,nm,sal): #variable initialization
        self.__id=empid
        self.__name=nm
        self.__sal=sal
        
    def __str__(self):
        return "Id : "+str(self.__id)+"\nName : "+self.__name+"\nSal : "+str(self.__sal)+"\n"
    
    def getId(self): 
        return self.__id
    
    def getName(self): #bhsbch
        return self.__name
    
    def setName(self,nm):#nscnsj
        self.__name=nm

    def setSal(self,sal):
        self.__sal=sal

if __name__=="__main__": 
    emp1=Employee(111,"Apurva",40000) 
    emp2=Employee(222,"Mahesh",45000) 
    emp3=Employee(333,"Ganesh",45000)
    emp4=Employee(444,"Nimish",40000)
    print(emp1)
    print(emp2)
    print(emp3)
    print(emp4)

