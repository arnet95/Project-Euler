def disc_probabilty(turns):
    probs = {(0, 0): 1}
    for i in xrange(1, turns + 1):
        new_probs = {(j, i-j): 0 for j in xrange(i+1)}
        for key in probs:
            red, blue = key
            new_probs[(red + 1, blue)] += probs[key]*i
            new_probs[(red, blue + 1)] += probs[key]
        probs = new_probs
    return probs

def main(n):
    d = disc_probabilty(n)
    total = sum(d.values())
    successes = sum(d[key] for key in d if key[0] < key[1])
    return total // successes
#If P(win) = a/b, maximum prize fund is b // a

print main(15)
