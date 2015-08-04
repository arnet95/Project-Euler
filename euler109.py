#Project Euler 109: Darts

singles = ["S" + str(i) for i in range(1, 21) + [25]]
doubles = ["D" + str(i) for i in range(1, 21) + [25]]
triples = ["T" + str(i) for i in xrange(1, 21)]
key = "0SDT"
all_values = singles + doubles + triples

one_checkout = [[i] for i in doubles]
two_checkout = [[i, j] for i in all_values for j in doubles]
three_checkout = [[i, j, k] for i in all_values for j in all_values for k in doubles]

vals = {i: [] for i in xrange(171)}
for checkout in one_checkout + two_checkout + three_checkout:
    s = sum(key.find(i[0]) * int(i[1:]) for i in checkout)
    vals[s].append(checkout)

def f(i):
    l = vals[i]
    new = []
    for e in l:
        if len(e) < 3:
            new.append(e)
        elif [e[1], e[0], e[2]] not in new:
            new.append(e)
    return len(new)

def main(n):
    return sum(f(i) for i in xrange(n))

print main(100)
