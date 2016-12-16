from itertools import permutations

def gen_lists(k, n):
    ret_set = set([])
    for perm in permutations(range(1, n+1), k):
        l1 = list(perm)[:k//2]
        l2 = list(perm)[k//2:]
        ret_set.add((tuple(sorted(l1)), tuple(sorted(l2))))
    return list(ret_set)

def needs_test(l1, l2):
    """Assume both lists sorted, and have equal length"""
    if sum(i < j for i, j in zip(l1, l2)) == len(l1):
        return False
    elif sum(j < i for i, j in zip(l1, l2)) == len(l1):
        return False
    else:
        return True

def main(n):
    s = 0
    for k in xrange(4, n+1, 2):
        s += sum(needs_test(i[0], i[1]) for i in gen_lists(k, n))
    return s // 2

print main(12)
