a = 2**30.403243784

def f(x):
    return int(a/(2**(x**2))) * (10**(-9))

def g(x):
    return f(f(x))

s1 = -1
while s1 != g(s1):
    s1 = g(s1)


s2 = f(-1)
while s2 != g(s2):
    s2 = g(s2)

print s1 + s2

#By some experimentation, we see that the sequence converges to an alternating
#sequence, and it does so very quickly. This means that at some point, since
#we're dealing with floating point numbers, we will have s = f(f(s)). What we
#do is to update the variables s1 and s2 until we have s1 = f(f(s1)) and s2 = f(f(s2)).
#Then we can simply add s1 and s2, and it will give us the right answer.
