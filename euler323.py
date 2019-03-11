
import numpy as np
from math import factorial

def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def p(i, j):
    if i > j:
        return 0
    else:
        return choose(32-i, j-i) / 2**(32-i)


#We set up the process as a Markov chain,
#and use a handy formula from Markov chain theory to compute the expected value
Q = []
for i in range(32):
    Q.append([p(i, j) for j in range(32)])
Q = np.array(Q)
print(sum(np.linalg.inv(np.identity(32) - Q)[0]))
