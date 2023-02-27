S = [290797]

def count(n):
    return (n-1)**2 - ((n-2)*(n-1)//2)

for i in range(1, 10**6+4):
    S.append(pow(S[-1], 2, 50515093))

def M_slow(n):
    products = sorted([S[i]*S[j] for i in range(0, n) for j in range(i+1, n)])
    return products[len(products)//2]

def product_count_lt(l, x):
    count = 0
    for i in range(len(l)):
        curr = l[i]
        if l[0]*curr >= x:
            count += 0
        elif l[-1]*curr < x:
            count += (len(l)-1)
        else:
            low = 0
            high = len(l) - 1
            mid = (low + high) // 2
            while (low + 1 < high):
                if l[mid]*curr < x:
                    low = mid
                else:
                    high = mid
                mid = (low + high) // 2
            count += (high) - (i <= low)
    return count//2
    return len([l[i]*l[j] for i in range(len(l)) for j in range(i+1, len(l)) if l[i]*l[j] < x])

def product_count_eq(l, x):
    for i in range(len(l)):
        curr = l[i]
        low = 0
        high = len(l) - 1
        mid = (low + high)//2
        while low <= high:
            if l[i]*l[mid] == x:
                if mid != i:
                    return True
                else:
                    break
            elif l[i]*l[mid] < x:
                low = mid+1
            else:
                high = mid-1
            mid = (low + high)//2
    return False 

def M(n):
    Ss = sorted(S[:n])
    limit = (count(n)-1)//2
    low = Ss[0]**2
    high = Ss[-1]**2
    x = (low+high)//2
    while True:
        ltcount = product_count_lt(Ss, x)
        if ltcount < limit:
            low = x + 1
        elif ltcount > limit:
            high = x - 1
        else:
            if product_count_eq(Ss, x):
                return x
            else:
                low = x + 1
        x = (low + high)//2
        print(low, high)

print(M(10**6+3))