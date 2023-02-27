from itertools import combinations, product

def generate_duodigits(d):
    numbers = set([])
    for comb in combinations(range(10), 2):
        a, b = map(str, sorted(comb))
        if a != "0":
            if a == b:
                numbers.add(int(a*d))
            else:
                for s in product((a, b), repeat=d):
                    numbers.add(int("".join(s)))
        else:
            if b != "0":
                for s in product((a, b), repeat=d-1):
                    numbers.add(int(b + "".join(s)))
    return sorted(list(numbers))

def generate_zero_duodigits(d):
    numbers = []
    for i in range(1, 10):
        b = str(i)
        for s in product(("0", b), repeat=d-1):
            numbers.append(int(b + "".join(s)))
    return sorted(numbers)

def zero_check(s):
    return all(i % 10 == 0 for i in s)

def D(k):
    s = set(range(100, k+1))
    result = sum(i for i in range(1, 100))
    d = 3
    while len(s) > 0:
        print(d, len(s), zero_check(s))
        if zero_check(s):
            duodigits = generate_zero_duodigits(d)
        else:
            duodigits = generate_duodigits(d)
        for duodigit in duodigits:
            new_found = set([])
            for i in s:
                if duodigit % i == 0:
                    if i not in new_found:
                        result += duodigit
                        new_found.add(i)
            for i in new_found:
                s.remove(i)
        d += 1
    return result



print(D(50000))