from __future__ import division
from math import acos, sqrt, pi

def angle(point1, point2):
    dot_prod = point1[0]*point2[0]+point1[1]*point2[1]
    length = sqrt(point1[0]**2+point1[1]**2)*sqrt(point2[0]**2+point2[1]**2)
    return acos(dot_prod/length)

successful = 0

with open("p102_triangles.txt", "r") as infile:
    for line in infile:
        triangle = [int(n) for n in line.split(',')]
        triangle1 = (triangle[0], triangle[1])
        triangle2 = (triangle[2], triangle[3])
        triangle3 = (triangle[4], triangle[5])
        s = angle(triangle1, triangle2) + angle(triangle2, triangle3) + angle(triangle3, triangle1)
        if (abs(s-2*pi) < 1E-13):
            successful += 1

print successful