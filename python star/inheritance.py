#most important topic
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showLang(self):
        print("The default language is python")

a=Employee("Rohan",400)
a.showDetails()
a2=Programmer("Mayank",410)
a2.showDetails( )
a2.showLang()
