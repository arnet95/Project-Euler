from math import sqrt

S = [290797]
for i in range(1, 4*10**6):
    S.append(pow(S[-1], 2, 50515093))


def dist(P1, P2):
    return sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

def d(k):
    P = sorted([(S[2*i], S[2*i+1]) for i in range(k)], key=lambda t:t[0])
    d = dist(P[0], P[1])
    for i in range(len(P)):
        if i % 10000 == 0:
            print(i)
        px, py = P[i]
        for j in range(i+1, len(P)):
            px1, py1 = P[j]
            if abs(px - px1) > d:
                break
            d = min(d, dist(P[i], P[j]))
    return d

print("%.9f" % d(2*10**6))
