from eulertools import modinv

a = 1504170715041707
m = 4503599627370517

curr_result = a
curr_smallest = m
curr_sum = 0

while curr_smallest > 10**8:
    if curr_result < curr_smallest:
        curr_smallest = curr_result
        curr_sum += curr_smallest
        print(curr_smallest)
    curr_result = (curr_result + a) % m


ainv = modinv(a, m)
l = [ainv*c % m for c in range(1, curr_smallest)]
while len(l) > 0:
    ind = min(range(len(l)), key=lambda i: l[i]) + 1
    curr_sum += ind
    print(ind)
    l = l[:ind-1]
print(curr_sum)
