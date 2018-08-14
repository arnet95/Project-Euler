from __future__ import division
from eulertools import primes, modinv

def is_square2(n):
  x = n // 2
  seen = set([x])
  while x * x != n:
    x = (x + (n // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True



def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

n = 1070379110497
print (1 + isqrt(1 + 2*(n**2-n)))//2


# results = []
#
# n = 1002802450650
# print is_square2(1 + 2*(n**2-n))
#
# for p in primes(30)[1:]:
#     quad_residues = set([x**2 % p for x in xrange(p)])
#     l = []
#     for n in xrange(p):
#         if (1 + 2*(n**2 - n)) % p in quad_residues:
#             l.append(n)
#     results.append([p, l])
#
# working_list = results[0]
# results = results[1:]
# while len(results) > 0:
#     adding = results[0]
#     results = results[1:]
#     m1 = working_list[0]
#     m2 = adding[0]
#     M = m1*m2
#     i1 = modinv(m2, m1)
#     i2 = modinv(m1, m2)
#     temp_results = []
#     for a in working_list[1]:
#         for b in adding[1]:
#             temp_results.append((a * i1 * m2 + b * i2 * m1) % M)
#     working_list = [M, sorted(temp_results)]
#
# i = working_list[0]*309
# condition = True
# while condition:
#     print i, "Start"
#     for j in working_list[1]:
#         n = i + j
#         if is_square2(1 + 2 * (n**2 - n)):
#             print n
#             condition = False
#             break
#     i += working_list[0]
