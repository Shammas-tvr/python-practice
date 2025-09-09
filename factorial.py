def factorial(x):
    if x ==0:
        return 1
    i=1
    fac=1
    while i <= x:
        fac=fac*i
        i+=1
    return fac
    
print(factorial(5))    