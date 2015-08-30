#Project Euler 120: Square remainders

def main(limit):
    r_max_sum = 0
    for a in xrange(3, limit+1):
        r_max = 2
        for n in xrange(1, 2*a, 2):
            r_max = max(r_max, (2*n*a)%(a**2))
        r_max_sum += r_max
    return r_max_sum

print main(1000)

#Expanding the binomials and reducing modulo a^2, we get that r = 2
#for all even n, and r = 2*n*a for all odd n. We use this to loop through
#all odd numbers up to 2*a, at which point we're guaranteed to have found a solution.
#We then simply sum up the maximal values we get.
