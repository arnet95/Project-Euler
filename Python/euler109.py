#Project Euler 109: Darts

singles = ["S" + str(i) for i in range(1, 21) + [25]]
doubles = ["D" + str(i) for i in range(1, 21) + [25]]
triples = ["T" + str(i) for i in xrange(1, 21)]
key = "0SDT"
all_values = singles + doubles + triples

one_checkout = [[i] for i in doubles]
two_checkouts = [[i, j] for i in all_values for j in doubles]
three_checkouts = [[i, j, k] for i in all_values for j in all_values for k in doubles]

checkout_values = {i: [] for i in xrange(171)}
for checkout in one_checkout + two_checkouts + three_checkouts:
    s = sum(key.find(i[0]) * int(i[1:]) for i in checkout)
    checkout_values[s].append(checkout)

#First, we generate all the different checkouts in all different orders
#(so it will contain duplicates, but only for the checkouts of length 3).
#This is doable since there are only 21 + 21*62 + 21*62*62 = 82047 possible
#checkouts in total (including duplicates), so it's clearly within the range of brute force.
#We store them by the value of the checkout.

def f(i):
    """Returns the number of checkouts starting with i points remaining."""
    l = checkout_values[i]
    two_or_less_checkouts = 0 #No crashes possible for checkouts of length 1 or 2.
    three_throws = []
    for e in l:
        if len(e) < 3:
            two_or_less_checkouts += 1
        elif [e[1], e[0], e[2]] not in three_throws: #The only possible crash.
            three_throws.append(e)
    return len(three_throws) + two_or_less_checkouts

def main(n):
    """Returns the number of checkouts starting with less than n points remaining."""
    return sum(f(i) for i in xrange(n))

print main(100)
