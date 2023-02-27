from math import isqrt

is_square = lambda n: isqrt(n)**2 == n

def power(t, a, n):
    if n == 0:
        return (1, 0)
    else:
        x, y = t
        t_sq = (x**2 + y**2*a, 2*x*y)
        if n % 2 == 1:
            x_res, y_res = power(t_sq, a, (n-1)//2)
            return (x*x_res + y*y_res*a, x*y_res + y*x_res)
        else:
            return power(t_sq, a, n//2)

def f(a, n):
    if is_square(a):
        print(a, pow(2*isqrt(a), n))
        return pow(2*isqrt(a), n)
    else:
        x, y = power((isqrt(a)+1, 1), a, n)
        print(a, x + isqrt(y**2*a))
        return x + isqrt(y**2*a)

def G(n):
    return sum(f(a, a**2) for a in range(1, n+1))

print(G(10))