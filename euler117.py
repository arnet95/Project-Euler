#Project Euler 117: Red, green, and blue tiles

mem = {1: 1, 2: 2, 3: 4, 4: 8}
#The base values

def f(n):
    if n in mem:
        return mem[n]
    else:
        #Representing seeing a black, a red, a green, and a blue tile respectively.
        tmp = f(n-1) + f(n-2) + f(n-3) + f(n-4)
    mem[n] = tmp
    return tmp

print f(50)

#We let f(n) represent the number of tilings of length n.
