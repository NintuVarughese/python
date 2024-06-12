class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print(self.name,self.age)
p1 = Person("Anakha",28)
p1.printvalue()
class Employe(Person):
    def __init__(self,name,age,department,salary):
        super().__init__(name,age)
        self.department = department
        self.salary = salary
    def printvalue(self):
        super().printvalue()
        print(self.department,self.salary)
p2 = Employe("ram",24,"cs",24000)
p2.printvalue()
    