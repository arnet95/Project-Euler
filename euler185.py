
conditions = [
("5616185650518293", 2),
("3847439647293047", 1),
("5855462940810587", 3),
("9742855507068353", 3),
("4296849643607543", 3),
("3174248439465858", 1),
("4513559094146117", 2),
("7890971548908067", 3),
("8157356344118483", 1),
("2615250744386899", 2),
("8690095851526254", 3),
("6375711915077050", 1),
("6913859173121360", 1),
("6442889055042768", 2),
("2326509471271448", 2),
("5251583379644322", 2),
("1748270476758276", 3),
("4895722652190306", 1),
("3041631117224635", 3),
("1841236454324589", 3),
("2659862637316867", 2),
("2321386104303845", 0)]

length = 16

def dfs(current_guess, current_conditions):
    print current_guess, current_conditions
    if max(i[1] for i in current_conditions) > length - len(current_guess):
        return None
    if len(current_guess) == length:
        if sum(i[1] for i in current_conditions) == 0:
            return current_guess
    else:
        for c in "0123456789":
            new_guess = current_guess + c
            new_conditions = []
            flag = True
            for i, j in current_conditions:
                if i[0] == c:
                    if j == 0:
                        flag = False
                    new_conditions.append((i[1:], j-1))
                else:
                    new_conditions.append((i[1:], j))
            if flag:
                a = dfs(new_guess, new_conditions)
                if a is not None:
                    return a

res = 0
for i in xrange(16):
    s = "0123456789"
    d = {c: 0 for c in s}
    for cond in conditions:
        if cond[1] > 0:
            d[cond[0][i]] += 1
        else:
            d[cond[0][i]] = 0
    print i, [(c, d[c]) for c in s]
    res += max(d.values())

print res
