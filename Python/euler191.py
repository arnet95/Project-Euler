#Project Euler 191: Prize Strings

mem = {}
def f(l, a, n):
    if (l, a, n) in mem:
        return mem[(l, a, n)]
    elif n == 0:
        b = (l < 2 and a < 3)
        mem[(l, a, n)] = b
        return b
    elif l == 2 or a == 3:
        mem[(l, a, n)] = 0
        return 0
    else:
        b = f(l+1, 0, n-1) + f(l, a+1, n-1) + f(l, 0, n-1)
        mem[(l, a, n)] = b
        return b

def main(n):
    return f(0, 0, n)

print main(30)

#Here we utilize a dynamic programming approach, where we let
#f(l, a, n) represent the number of "prize strings" of length n
#with l number of late arrivals before the beginning of the string
#and a number of consecutive absences just before the beginning of the string.
#f can be described as f(l, a, n) = f(l+1, 0, n-1) + f(l, a+1, n-1) + f(l, 0, n-1)
#(as a result of seeing an L, an A, and an O in the current position in the string)
#and certain base cases for l == 2, a == 3 and n == 0.
