#Project Euler 162: Hexadecimal numbers

mem = {}
def f(n, one, zero, A):
    if (n, one, zero, A) in mem:
        return mem[(n, one, zero, A)]
    else:
        if n == 0:
            tmp = (one * zero * A)
        else:
            tmp = f(n-1, 1, zero, A) + f(n-1, one, 1, A) + f(n-1, one, zero, 1)
            tmp += 13*f(n-1, one, zero, A)
        mem[(n, one, zero, A)] = tmp
        return tmp

#f(n, one, zero, A) describes the number of hexadecimal numbers of length n
#containing at least one number of 1s, zero number of 0s, A number of As.
#f can be described recursively as follows:
#If n == 0, we return whether we've seen at least one 1, one 0, and one A.
#Otherwise, we return f(n-1, 1, zero, A) + f(n-1, one, 1, A) + f(n-1, one, zero, 1)
#+ 13*f(n-1, one, zero, A), representing seeing a 1, a 0 and an A or
#something else, respectively.
#If we memoize this function, we get the answer immediately.

def main(n):
    s = 0
    for i in xrange(1, n+1):
        s += f(i-1, 1, 0, 0) #Begins with a 1
        s += f(i-1, 0, 0, 1) #Begins with an A
        s += 13*f(i-1, 0, 0, 0) #Begins with something else, but not 0.
    return hex(s)[2:].upper() #Conversion to hexadecimal

print main(16)
