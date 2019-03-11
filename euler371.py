import numpy as np

#A Markov chain approach

def p(t1, t2):
    i, b = t1
    j, c = t2
    if b == 0:
        if (j, c) == (i, 1):
            return 1/1000.
        elif (j, c) == (i, 0):
            return (i+1)/1000.
        elif (j, c) == (i+1, 0):
            return (1000-2*i-2)/1000.
        else:
            return 0.
    else:
        if (j, c) == (i, 1):
            return (i+1)/1000.
        elif (j, c) == (i+1, 1):
            return (1000-2*i-2)/1000.
        else:
            return 0.

Q = []
for i in range(0, 500):
    for b in [0, 1]:
        Q.append([p((i, b), (j, c)) for j in range(0, 500) for c in [0, 1]])
Q = np.array(Q)
print(round(sum(np.linalg.inv(np.identity(1000)-Q)[0]), 8))
