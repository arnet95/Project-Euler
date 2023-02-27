from eulertools import prod

set_size = lambda l: prod(l) - sum(l) + len(l)

def f(limit):
    d = {}
    l = [2, 2]
    while True:
        result = set_size(l)
        if result in d:
            d[result] = min(d[result], prod(l))
        else:
            d[result] = prod(l)
        flag = False
        for index in range(len(l)-1, -1, -1):
            lprime = l[:]
            lprime = l[:index] + [l[index]+1]*(len(l)-index)
            if set_size(lprime) <= limit:
                flag = True
                l = lprime[:]
                break
        if not flag:
            l = [2]*(len(l)+1)
            if set_size(l) > limit:
                break
    return sum(set(d.values()))

print(f(12000))
