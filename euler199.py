from math import sqrt

def new_curvature(k1, k2, k3):
    return k1+k2+k3+2*sqrt(k1*k2+k2*k3+k1*k3)


def main(N):
    circles = []
    r = 2*sqrt(3) - 3
    middle_gaps = [(1/r, 1/r, 1/r)]
    for _ in xrange(N):
        new_gaps = []
        for gap in middle_gaps:
            curv1, curv2, curv3 = gap
            curvature = new_curvature(curv1, curv2, curv3)
            new_gaps.append((curv1, curv2, curvature))
            new_gaps.append((curv1, curv3, curvature))
            new_gaps.append((curv2, curv3, curvature))
            circles.append(1/curvature)
        middle_gaps = new_gaps

    result = sum(rc**2 for rc in circles)
    circles = [r]
    outside_gaps = [(-1, 1/r, 1/r)]
    for _ in xrange(N):
        new_gaps = []
        for gap in outside_gaps:
            curv1, curv2, curv3 = gap
            curvature = new_curvature(curv1, curv2, curv3)
            new_gaps.append((curv1, curv2, curvature))
            new_gaps.append((curv1, curv3, curvature))
            new_gaps.append((curv2, curv3, curvature))
            circles.append(1/curvature)
        outside_gaps = new_gaps


    result += 3*sum(rc**2 for rc in circles)
    return 1 - result

print round(main(10), 8)
