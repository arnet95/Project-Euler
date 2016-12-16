#Project Euler 72: Counting fractions
from eulertools import totient_gen

#After thinking about the problem for a while, one should realize that the
#number of new reduced proper fractions added with denominator d is just
#phi(d) (Euler's totient function). And then the answer is just the sum of
#phi(d) for d from 2 and up to n.

#We take the relevant function from our toolbox and get the answer very quickly.

def main(n):
    return sum(totient_gen(n)[2:])

print main(10**6)
