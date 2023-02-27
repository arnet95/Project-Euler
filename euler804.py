from eulertools import isqrt

f = lambda x, y: x**2 + x*y + 41*y**2

def T(N):
    result = 2*isqrt(N)
    for y in range(1, N+1):
        if 163*y**2 > 4*N:
            break
        tmp = isqrt(4*N-163*y**2)
        high = (-y + tmp)//2
        low = (-y - tmp)//2
        low += (f(low, y) > N)
        result += 2*(high - low + 1)
    return result

print(T(10**16))

