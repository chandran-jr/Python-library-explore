fib_store = {}

def  fib(n):
    if n == 1:
        fib_store[n] = 0
        return 0
    
    elif n == 2:
        fib_store[n] = 1
        return 1
    
    else:
        fibl = 0
        fibr = 0
        
        if n-2 in fib_store.keys():
            fibl = fib_store[n-2]
            
        else:
            fibl = fib(n-2)
            fib_store[n-2] = fibl
            
        if n-1 in fib_store.keys():
            fibr = fib_store[n-1]
            
        else:
            fibr = fib(n-1)
            fib_store[n-1] = fibr
        return fibl + fibr
    

n= input("Input n for the nth term required ")
n= int(n)
k= fib(n)
print(k)
