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
horisontal = lambda line : line[1] == line[3]

def is_interior(pt, line):
    vert_cond = min(line[1], line[3]) < pt[1] and pt[1] < max(line[1], line[3])
    horis_cond = min(line[0], line[2]) < pt[0] and pt[0] < max(line[0], line[2])
    if vertical(line):
        return vert_cond
    elif horisontal(line):
        return horis_cond
    else:
        return vert_cond and horis_cond



def true_intersection(line1, line2):
    if vertical(line1) or vertical(line2):
        if vertical(line1) and vertical(line2):
            return (False,)
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
            return (is_interior((x, y), line2) and is_interior((x, y), line1), x, y)

    else:
        x0, y0, x1, y1 = line1
        a = Fraction(y1-y0, x1-x0)
        b = y0 - a*x0
        x0, y0, x1, y1 = line2
        c = Fraction(y1-y0, x1-x0)
        d = y0 - c*x0
        if a == c:
            return (False,)
        else:
            x = (d - b)/(a - c)
            y = a*x + b
            return (is_interior((x, y), line1) and is_interior((x, y), line2), x, y)


def main(n):
    lines = generate_lines(n)
    intersection_points = set([])
    for i in xrange(n):
        for j in xrange(i+1, n):
            res = true_intersection(lines[i], lines[j])
            if res[0]:
                intersection_points.add((res[1], res[2]))
    return len(intersection_points)

print main(5000)
