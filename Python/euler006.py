#Project Euler 6: Sum square difference

def one_liner(n):
    """Straightforward expression comprehension"""
    return sum(i for i in xrange(1, n+1))**2 - sum(i**2 for i in xrange(1, n+1))

def efficient(n):
    """Uses the sum formulas for powers"""
    return (n**4 + 2*n**3 + n**2)//4 - (n*(n+1)*(2*n+1))//6

print efficient(10**2)
