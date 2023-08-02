# no acces modifer in python but  their is a way to use them
# just convention h 
class Employee:
    def __init__(self):
        self.__name="mayank"
        self.age=21

a=Employee()
# print(a.__name) cannot be accessed directly
print(a._Employee__name) # can be accessed indirectly name magling
print(a.__dir__())


