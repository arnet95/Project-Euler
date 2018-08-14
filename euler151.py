from itertools import product

def f(s):
    result = 0
    d = {2: 1, 3: 1, 4: 1, 5: 1}
    count = 4
    for c in s:
        if count == 1:
            result += 1
        if d[int(c)] == 0:
            return "Not valid"
        d[int(c)] -= 1
        for i in xrange(int(c)+1, 6):
            d[i] += 1
        count += (4 - int(c))
    return result

good_count = 0
result = 0
for s in product("2345", repeat=14):
    if s.count("2") == 1:
        if s.count("3") == 2:
            if s.count("4") == 4:
                a = f(s)
                if a != "Not valid":
                    good_count += 1
                    result += a
#print result, good_count
print result / float(good_count)
