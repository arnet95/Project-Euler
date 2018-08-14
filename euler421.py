def degree(poly):
    return max(poly.keys())

def poly_add(poly1, poly2):
    d = {}
    for degree in poly1:
        if degree in d:
            d[degree] += poly1[degree]
        else:
            d[degree] = poly1[degree]
    for degree in poly2:
        if degree in d:
            d[degree] += poly2[degree]
        else:
            d[degree] = poly2[degree]
    return {key: d[key] for key in d if d[key] != 0}

def poly_division(n, d):
    q = {}
    r = n
    while r != {0: 0} and degree(r) >= degree(d):
        pass

#def gcd(a, b):
