class MYclass:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"value is {self.value}")
    
    @property
    def ten_value(self): #getter
        return 10*self.value
    
    
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
    
obj=MYclass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()
