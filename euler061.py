#Project Euler 61: Cyclical figurate numbers

def g(l):
    postfixes = [i % 100 for i in l]
    prefixes = [i // 100 for i in l]
    return sorted(prefixes) == sorted(postfixes)


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

all_nums = triangles + squares + pentagonals + hexagonals + heptagonals + octagonals


prefixes = list(set([num // 100 for num in all_nums]))
postfixes = list(set([num % 100 for num in all_nums]))

list_of_shapes = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]


old_prefix_length = len(prefixes)
old_postfix_length = len(postfixes)

while old_prefix_length != old_postfix_length:
    new_shapes = []
    for shape in list_of_shapes:
        l = []
        for num in shape:
            if num // 100 in postfixes and num % 100 in prefixes:
                l.append(num)
        new_shapes.append(l)

    all_nums = [item for shapes in new_shapes for item in shapes]

    prefixes = list(set([num // 100 for num in all_nums]))
    postfixes = list(set([num % 100 for num in all_nums]))
    list_of_shapes = new_shapes
    old_prefix_length = len(prefixes)
    old_postfix_length = len(postfixes)

triangles = list_of_shapes[0]
squares = list_of_shapes[1]
pentagonals = list_of_shapes[2]
hexagonals = list_of_shapes[3]
heptagonals = list_of_shapes[4]
octagonals = list_of_shapes[5]

for triangle in triangles:
    for square in squares:
        for pentagon in pentagonals:
            for hexagon in hexagonals:
                for heptagon in heptagonals:
                    for octagon in octagonals:
                        if g([triangle, square, pentagon, hexagon, heptagon, octagon]):
                            l.append([triangle, square, pentagon, hexagon, heptagon, octagon])


def f(l):
    for n in l:
        if (n % 100) * 100 + (n // 100) in l:
            return False
    return True

new = []
for l in a:
    if f(l):
        new.append(l)
print sum(new[0])

#Runs in over 30 minutes, currently. Doing a very bad brute force approach.
