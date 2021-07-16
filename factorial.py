import math

# Factorial utilizando la función math de python
def factorialMath(n):
    return(math.factorial(n))

# Factorial usando una función recursiva
def factorialRecursive(n):     
    return 1 if (n==1 or n==0) else n * factorialRecursive(n - 1)

# Factorial usando iteraciones
def factorialIterative(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Factorial usando iteraciones
def factorialIterative2(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact