#An Arithmetic Geometric sequence

#After a bunch of fiddling with arithmetic and geometric series,
#one can get a closed form expression for the sum in terms of r.
#Then, it's simply a matter of using some root finding method to find the answer.
#I used the bisection method with the choices of initial endpoints
#chosen manually by inspecting the problem. The solution has to be more than 1,
#but also less than 2. Then one can choose bounds such that one does not get
#neither a zero division error nor an overflow error when the program is run.

s = -600000000000

def g(r):
    """Returns s(5000)- (-600000000000) for the given value of r"""
    return 900*(1-r**5000)/(1-r) - 3*(1-r**5000)/((1-r)**2) + 15000*(r**5000)/(1-r) - s

def bisection(a, b, tolerance=1e-13):
    c = (a+b)/2.
    while (b-a)/2. > tolerance:
        if g(c) == 0:
            return c
        elif g(a)*g(c) < 0:
            b = c
        else:
            a = c
        c = (a+b)/2.
    return c

print "%.12f" % bisection(1.0000001, 1.1)
