class person:
    def __init__(self,name,occ):
        print("hey i am a person")
        self.name =name
        self.occ=occ
    
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
        
a = person("Mayank","Developer")
b=person("Charu","HR")
a.info()
b.info()

# object create hoo gya 
    # a.info()      
    