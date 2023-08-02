
# print("decoraters")


    
def greet(fx):
    def mfx():
        print("Good Mornig")
        fx()
        print("This for using this function")
    return mfx
    
@greet
def hello():
    print("hello world")
# @greet 
def add(a,b):
    print(a+b)
    

    
# greet(hello)()
hello()
greet(add(1,2))




