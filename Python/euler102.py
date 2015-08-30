#Project Euler 102: Triangle containment
from __future__ import division
from math import acos, sqrt, pi

def angle(point1, point2):
    """The angle between the line through (0, 0) and point1 and the line
       between (0, 0) and point2, using the cosine formula for the angle."""
    dot_prod = point1[0]*point2[0]+point1[1]*point2[1]
    length = sqrt(point1[0]**2+point1[1]**2)*sqrt(point2[0]**2+point2[1]**2)
    return acos(dot_prod/length)

successful = 0

with open("../input/p102_triangles.txt", "r") as infile:
    for line in infile:
        triangle = [int(n) for n in line.split(',')]
        point1 = triangle[:2]
        point2 = triangle[2:4]
        point3 = triangle[4:]
        s = angle(point1, point2) + angle(point2, point3) + angle(point3, point1)
        if (abs(s-2*pi) < 1E-13):
            successful += 1
        #We check whether the sum of the angles created by the lines to the corners
        #equals 2pi radians. It will do this only when the triangle contains (0, 0).

print successful
