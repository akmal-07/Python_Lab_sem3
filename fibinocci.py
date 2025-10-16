def fib(n):
    if (n<1) :
        return -1 
    elif(n==1):
        return 0
    elif(n==2) :
        return 1
    else :
        return fib(n-1)+fib(n-2)
    
n = input("enter the nth :")
print(fib(n))    
""""a class is a way to goup data and function together. it defines how an object shaould behave and what data it could store
eg : 
    class = blueprint of car                  
    object = actual built of a car"""
