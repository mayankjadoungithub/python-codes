print("factorial program by recusion")
n=int(input("enter number:34"))
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(n))