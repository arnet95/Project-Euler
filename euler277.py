#Project Euler 277: A Modified Collatz sequence

def main(limit, string):
    k = 1
    c, d = 1, 0
    for char in string:
        if char == "D":
            e, f = 1, 0
        elif char == "U":
            e, f = 4, 2
        else:
            e, f = 2, -1
        c, d = c*e, e*d + f*(3**(k-1))
        k += 1
    n = (c * limit + d) // (3**(k-1)) + 1
    while (n * (3**(k-1)) - d) % c != 0:
        n += 1
    return (n * (3**(k-1)) - d) // c

print main(10**15, "UDDDUdddDDUDDddDdDddDDUDDdUUDd")
