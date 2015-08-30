#Project Euler 173: Using up to one million tiles how many different
#"hollow" square laminae can be formed?

def f(n):
    s = 0
    hole_size = 1

    while hole_size < n // 4:
        k = 1
        while 4*k*(hole_size+k) <= n:
            k += 1
            s += 1
        hole_size += 1

    return s

print f(1000000)
