#An Arithmetic Geometric sequence

s = -600000000000

def g(r):
    return 900*(1-r**5000)/(1-r) - 3*(1-r**5000)/((1-r)**2) + 15000*(r**5000)/(1-r) - s

#Found manually, could be found by root finding method. For example, bisection.
print int(g(1.002322108632876))
