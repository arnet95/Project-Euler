import numpy as np

def P(i):
    if i == 1:
        return [19/36., 8/36., 1/36.] + [0]*47
    elif i == 2:
        return [8/36., 18/36., 8/36., 1/36.] + [0]*46
    elif i == 49:
        return [0]*46 + [1/36., 8/36., 19/36., 8/36.]
    elif i == 50:
        return [0]*47 + [2/36., 16/36., 18/36.]
    else:
        return [0]*(i-3)+[1/36., 8/36., 18/36., 8/36., 1/36.] + [0]*(48-i)

Q = [P(i) for i in xrange(1, 51)]
Q = np.array(Q)
print(round(sum(np.linalg.inv(np.identity(50) - Q)[49]), 10))
