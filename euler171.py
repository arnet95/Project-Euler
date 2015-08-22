#Project Euler 171: Finding numbers for which the sum of the squares of the digits is a square

def is_square(n):
    return ((n ** 0.5) % 1) == 0
    #We can use this since the values we check are all less than 2000.
    
def buckets(k):
    d = {i**2: (i, 1) for i in xrange(10)}
    counter = 1
    while counter < k:
        new_d = {}
        for elem in d:
            si, ni = d[elem]
            for i in xrange(10):
                sq = i*i
                res = elem + sq
                if res in new_d:
                    new_d[res] = (i * (10**counter ) * ni + si + new_d[res][0], ni + new_d[res][1])
                else:
                    new_d[res] = (i * (10**counter ) * ni + si, ni)
        d = new_d
        counter += 1
    return d

def main(k):
    d = buckets(k)
    return sum(d[key][0] for key in d if is_square(key))

print main(20)
