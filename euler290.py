#Project Euler 290: Digital Signature

def digit_sum(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

n = 0
while True:
    if digit_sum(n) == digit_sum(137*n):
        if digit_sum(n) == 81:
            print digit_sum(n)
    n += 9
