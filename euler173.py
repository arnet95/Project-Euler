#Project Euler 173: Using up to one million tiles how many different
#"hollow" square laminae can be formed?

def f(n):
    s = 0
    m = 1

    while m < n/4:
        k = 0
        while 4*k*(m+k) <= n:
            k += 1
        s += (k-1)
        m += 1

    return s

print f(1000000)
