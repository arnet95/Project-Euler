from itertools import combinations

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

#conditions = [("51545", 2),("39458", 2),("90342", 2),("70794", 0),("34109", 1),("12531", 1)]
#length = 5

def f(conditions, excluded):
    str_length = len(excluded)
    if any(condition[1] > str_length for condition in conditions):
        return None
    if str_length == 0:
        return ""
    if any(len(s) == 10 for s in excluded):
        return None
    if len(conditions) == 0:
        return "".join([list(set([str(j) for j in range(10)]) - exclude_set)[0] for exclude_set in excluded])
    conditions = sorted(conditions, key=lambda x: x[1])
    #print(conditions, excluded, str_length)
    #Second: Loop over all possible correct digit assignments
    numbers, num_correct = conditions[0]
    for indices in combinations(range(str_length), num_correct):
        #Check that none of the indices are not excluded
        if all(numbers[i] not in excluded[i] for i in indices):
            not_indices = [i for i in range(str_length) if i not in indices]
            #Create new parameters
            new_conditions = []
            for condition in conditions[1:]:
                new_nums = "".join([condition[0][i] for i in not_indices])
                new_correct = condition[1] - sum(numbers[i] == condition[0][i] for i in indices)
                new_conditions.append((new_nums, new_correct))
            new_excluded = []
            for i in not_indices:
                new_excluded.append(set(list(excluded[i]) + [numbers[i]]))
            rec_result = f(new_conditions, new_excluded)
            if rec_result is not None:
                ret_string = ""
                j = 0
                for i in range(str_length):
                    if i in indices:
                        ret_string += numbers[i]
                    else:
                        ret_string += rec_result[j]
                        j += 1
                return ret_string
    return None


print(f(conditions, [set([]) for i in range(length)]))
