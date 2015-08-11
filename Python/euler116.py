#Project Euler 116: Red, green or blue tiles

mem = {}
def f(n, used, k):
    if (n, used, k) in mem:
        return mem[(n, used, k)]
    elif n < k:
        a = used
    else:
        a = f(n-1, used, k) + f(n-k, True, k)
    mem[(n, used, k)] = a
    return a

def main(n):
    return f(n, False, 2) + f(n, False, 3) + f(n, False, 4)

print main(50)

#We let f(n, used, k) represent the number of tilings of length n
#using tiles of length 1 or length k, and let the boolean used represent whether
#we've used a tile of length k previously in that tiling. If we reach a state
#when n < k, we can only tile the rest of the tiling using black tiles, so then
#we return whether or not we've used a tile of length k in the tiling.
#In the cases when n >= k, we can choose a tile of length 1, or a tile of length
#k, and recursively call f accordingly. If we memoize this function,
#the problem is solved in <1 ms.
