from eulertools import primes, isqrt, prod

def mobius_gen(n):
    mobius_list = [1 for _ in range(n+1)]
    for p in primes(n+1):
        for i in range(p, n+1, p):
            mobius_list[i] *= (-1)
        k = 2
        while p**k <= n:
            for i in range(p**k, n+1, p**k):
                mobius_list[i] = 0
            k += 1
    return mobius_list




def sqfcount(n, mobius):
    count = 0
    for k in range(1, isqrt(n)+1):
        count += (n//(k**2))*mobius[k]
    return count

def generate_exponents(ps, N):
    if len(ps) == 1:
        results = []
        power = 2
        while ps[0]**power <= N:
            results.append((power,))
            power += 2
        return results
    else:
        #Assume ps is in ascending order
        results = []
        initial_power = 2
        while ps[0]**initial_power <= N:
            for tup in generate_exponents(ps[1:], N//(ps[0]**initial_power)):
                results.append((initial_power,) + tup)
            initial_power += 2
        return results

def C(k, N, ps, mobius):
    result = 0
    l = list(range(k))
    while True:
        #Try even powers of current list
        curr_ps = [ps[i] for i in l]
        for powers in generate_exponents(curr_ps, N):
            result += sqfcount(N//prod([curr_ps[i]**powers[i] for i in range(k)]), mobius)

        #Generate next l
        idx = k-1
        l[idx] += 1
        while l[-1] < len(ps) and prod(ps[i] for i in l)**2 > N and idx > 0:
            idx -= 1
            l = l[:idx] + list(range(l[idx]+1, l[idx] + k - idx + 1))
        #Break if next l does not exist
        if l[-1] >= len(ps) or prod(ps[i] for i in l)**2 > N:
            break

    return result


#print(C(1, 10**8, primes(10**4), mobius_gen(10**4//2)))

def f(N):
    mobius = mobius_gen(isqrt(N)//2)
    prime_list = primes(isqrt(N))

    results = {}
    k = 1
    ck = C(k, N, prime_list, mobius)
    while ck > 0:
        print(k)
        results[k] = ck
        k += 1
        ck = C(k, N, prime_list, mobius)
    results[0] = N - sum(results.values())
    return prod(results.values()) % (10**9 + 7)

print(f(10**16))