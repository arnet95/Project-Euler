#Project Euler 114: Counting block combinations I

mem = {}
def f(n, red):
    if (n, red) in mem:
        return mem[(n, red)]
    elif n < 3:
        #We can only fill the rest of the block with all black,
        #so it's only one possible way to fill the block.
        a = 1
    elif red:
        #We must see a black, since we last saw a red.
        a = f(n-1, False)
    else:
        #We can see a black block (first case), or a red block of an arbitrary length >= 3 (second case).
        a = f(n - 1, False) + sum(f(i, True) for i in xrange(n-3, -1, -1))
    mem[(n, red)] = a
    return a

print f(50, False)
#We let f(n, red) return the number of ways a row measuring n units in length
#if the last block was red or not. It can be described recursively, with the cases
#further commented above. Simply memoize it, and the answer pops out in about 1 ms.
