#Project Euler 122: Efficient exponentiation

def main(n):
    remaining = range(2, n+1)
    mk = {1: 0}
    curr = [[1]]
    while remaining != []:
        new = []
        print len(curr)
        for l in curr:
            for a in l:
                b = l[-1]
                s = a + b
                if s <= n:
                    if l + [s] not in new:
                        new.append(l + [s])
                        if s in remaining:
                            mk[s] = len(l)
                            remaining.remove(s)
            if remaining == []:
                break
        curr = new
        print remaining
    return sum(mk[i] for i in xrange(1, n+1))

print main(100)
