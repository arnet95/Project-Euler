#Project Euler 61: Cyclical figurate numbers

triangles = [(i*(i+1))/2 for i in xrange(150)]
squares = [i**2 for i in xrange(100)]
pentagonals = [(i*(3*i-1))/2 for i in xrange(100)]
hexagonals = [i*(2*i-1) for i in xrange(100)]
heptagonals = [(i*(5*i-3))/2 for i in xrange(100)]
octagonals = [i*(3*i-2) for i in xrange(100)]

f = lambda x: (1000 <= x <= 9999) and (x % 100 > 9)

triangles = filter(f, triangles)
squares = filter(f, squares)
pentagonals = filter(f, pentagonals)
hexagonals = filter(f, hexagonals)
heptagonals = filter(f, heptagonals)
octagonals = filter(f, octagonals)

all_nums = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
print all_nums
