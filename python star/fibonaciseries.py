print("program of febonaci series")
n=int(input("enter number:"))
# a=0
# b=1
# c=a+b
def fibonaci(n):
    if(n<0):
        print("incoorect")
    elif(n==0 ):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    
print("fibonaci series is :",fibonaci(n))