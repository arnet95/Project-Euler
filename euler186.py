S_mem = {}
def S(k):
    if k in S_mem:
        return S_mem[k]
    elif 1 <= k and k <= 55:
        result = (100003 - 200003*k + 300007*k**3) % 1000000
        S_mem[k] = result
        return result
    else:
        result = (S(k-24) + S(k-55)) % 1000000
        S_mem[k] = result
        return result

#Using a disjoint-set structure

parent = [i for i in xrange(10**6)]
size = [1 for i in xrange(10**6)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if size[xroot] < size[yroot]:
        xroot, yroot = yroot, xroot
    parent[yroot] = xroot
    size[xroot] = size[xroot] + size[yroot]

count_successful = 0
k = 1
while size[find(524287)] < 990000:
    caller = S(2*k-1)
    called = S(2*k)
    if caller != called:
        if find(caller) != find(called):
            union(caller, called)
        count_successful += 1
    k += 1

print count_successful
