class person:

    def __init__(self,n,o):
        print("hey i am person")
        self.name=n
        self.occ=o
    def info(self):
      print(f"{self.name} is a {self.occ}")
  
a=person("MPS","DEVOPS")
b=person("Divya","HR")  
a.info()
b.info()
