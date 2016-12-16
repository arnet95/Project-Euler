from fractions import *

def generate_lines(n):
    s = [290797]
    for i in xrange(4*n):
        s.append(pow(s[i], 2, 50515093))
    t = [c % 500 for c in s]
    lines = []
    for i in xrange(n):
        lines.append(tuple(t[4*i+1:4*i+5]))
    return lines

vertical = lambda line : line[0] == line[2]

def is_endpoint(pt, line):
    x, y = pt
    x0, y0, x1, y1 = line
    return ((x, y) == (x0, y0)) or ((x, y) == (x1, y1))

def is_interior(pt, line):
    return not(is_endpoint(pt, line))


def true_intersection(line1, line2):
    if vertical(line1) or vertical(line2):
        if vertical(line1) and vertical(line2):
            return False
        else:
            if vertical(line2):
                line1, line2 = line2, line1
            #Now line1 is the vertical one
            a = line1[0]
            x0, y0, x1, y1 = line2
            c = Fraction(y1-y0, x1-x0)
            d = y0 - c*x0
            x = a
            y = c*a+d
            x0, y0, x1, y1 = line1
            return is_interior((x, y), line2) and is_interior((x, y), line1)

    else:
        x0, y0, x1, y1 = line1
        a = Fraction(y1-y0, x1-x0)
        b = y0 - a*x0
        x0, y0, x1, y1 = line2
        c = Fraction(y1-y0, x1-x0)
        d = y0 - c*x0
        if a == c:
            return False
        else:
            x = (d - b)/(a - c)
            y = a*x + b
            return is_interior((x, y), line1) and is_interior((x, y), line2)

test_lines = [[27, 44, 12, 32], [46, 53, 17, 62], [46, 70, 22, 40]]

def test():
    lines = test_lines
    n = len(lines)
    count = 0
    for i in xrange(n):
        for j in xrange(i+1, n):
            if true_intersection(lines[i], lines[j]):
                count += 1
    return count

def main(n):
    lines = generate_lines(n)
    print len(lines)
    count = 0
    for i in xrange(n):
        for j in xrange(i+1, n):
            if true_intersection(lines[i], lines[j]):
                count += 1
    return count

print test()
print main(5000)
