from itertools import product

def f(conditions, settled, tot):
    if conditions == []:
        return 2**(tot-settled)
    else:
        set_of_possible_elements = set.union(*conditions)
        s = max(set_of_possible_elements, key=lambda i: sum(i in condition for condition in conditions))
        new_conditions1 = []
        for condition in conditions:
            if s not in condition:
                new_conditions1.append(condition)
        new_conditions2 = []
        t_list = set([])
        for condition in conditions:
            if s in condition:
                t_list.add(list(condition - set([s]))[0])
        for condition in conditions:
            if all(t not in condition for t in t_list):
                new_conditions2.append(condition)
        return f(new_conditions1, settled+1, tot) + f(new_conditions2, settled+1+len(t_list), tot)

def logic_comp(t):
    a, b, c, d, e, f = t
    return (b, c, d, e, f, a ^ (b & c))

def main():
    found = set([])
    list_of_disjoint_chains = []
    for t in product([0, 1], repeat=6):
        if t not in found:
            current_found_set = set([t])
            found.add(t)
            l = [set([t, logic_comp(t)])]
            while logic_comp(t) not in current_found_set:
                t = logic_comp(t)
                found.add(t)
                current_found_set.add(t)
                l.append(set([t, logic_comp(t)]))
            list_of_disjoint_chains.append(l)
    result = 1
    for l in list_of_disjoint_chains:
        if len(l) == 1:
            result *= 1
        else:
            result *= f(l, 0, len(l))
    return result

print main()
