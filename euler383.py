from math import factorial

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return digits[::-1]

def f5(n):
    count = 0
    while n % 5 == 0:
        count += 1
        n //= 5
    return count

def T5(n):
    count = 0
    for i in range(1, n+1):
        if f5(factorial(2*i-1)) < 2*f5(factorial(i)):
            count += 1
            print(i, numberToBase(i, 5))
    return count

print(T5(10**3))

#For the condition to be satisfied, we require that 5 divides i.
