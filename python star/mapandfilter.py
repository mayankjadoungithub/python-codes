# def cube(x):
#     return x*x*x

# print(cube(2))

l=[1,2,3,5,7,8,9]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(lambda x: x*x*x,l))
print(newl)
    
    
#FILTER
def filter_function(a):
    return  a>3

newl1=list(filter(filter_function,l))
print(newl1)
    
from functools import reduce
number=[1,2,3,4,5]
def mysum(x,y):
    return x+y
sum = reduce(mysum,number)

print(sum)    