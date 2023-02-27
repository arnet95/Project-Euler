from itertools import product

S_mem = {}
loc_map = {"FREE": 0, "FARE": 1, "AREA": 2, "REEF": 3}

#initalise S_mem:
for t in product("FARE", repeat=4):
    s = "".join(t)
    l = [False]*4
    if s in loc_map:
        l[loc_map[s]] = True
    seen = tuple(l)
    S_mem[(4, s, seen)] = 1

#seen = (free, fare, area, reef)


def S(n, last_four, seen):
    if (n, last_four, seen) in S_mem:
        return S_mem[(n, last_four, seen)]
    elif n == 4:
        S_mem[(n, last_four, seen)] = 0
        return 0
    else:
        if last_four in loc_map:
            if seen[loc_map[last_four]]:
                new_seen = list(seen)
                new_seen[loc_map[last_four]] = False
                new_seen = tuple(new_seen)
                result = 0
                for c in "FARE":
                    result += S(n-1, c + last_four[:-1], new_seen)
                S_mem[(n, last_four, seen)] = result
                return result
            else:
                S_mem[(n, last_four, seen)] = 0
                return 0
        else:
            result = 0
            for c in "FARE":
                result += S(n-1, c + last_four[:-1], seen)
            S_mem[(n, last_four, seen)] = result
            return result

def f(n):
    result = 0
    for t in product("FARE", repeat=4):
        s = "".join(t)
        result += S(n, s, (True, True, True, True))
    return result


print(f(30))
