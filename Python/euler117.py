#Project Euler 117: Red, green, and blue tiles

mem = {1: 1, 2: 2, 3: 4, 4: 8}
def f(n):
    if n in mem:
        return mem[n]
    else:
        tmp = f(n-1) + f(n-2) + f(n-3) + f(n-4)
    mem[n] = tmp
    return tmp

print f(50)

#We let f(n) represent the number of tilings of length n. We have for the base values:
# f(1) = 1: B
# f(2) = 2: BB, R
# f(3) = 4: BBB, RB, BR, G
# f(4) = 8: BBBB, RBB, BRB, BBR, RR, BG, GB, Bl

#For the recursive case, f(n) is given by the number of tilings which begin with
#a black tile, a red tile, a green tile and a blue tile, which means that
#f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4), representing all the tiles.
