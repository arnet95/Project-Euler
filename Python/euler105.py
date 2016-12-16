from itertools import product

def is_special(l):
    l = sorted(l)
    k = len(l)
    #Criterion 2
    #The only way that a set can violate criterion 2 is if the n/2 biggest elements
    #have greater sum than the remaining elements.
    if k % 2 == 0:
        if sum(l[:k//2]) <= sum(l[k//2+1:]):
            return False
    else:
        if sum(l[:k//2+1]) <= sum(l[k//2+1:]):
            return False
    #Criterion 1
    #This is a straightforward brute force approach. One generates a tuple
    #of 12 elements, each in [-1, 0, 1], which decides whether a number should
    #be added, subtracted or not included in the sum.
    #If any of these then sum to 0, criterion 1 is violated.
    for tup in product([-1,0,1], repeat=k):
        if list(tup).count(0) != k:
            if sum(i*j for i, j in zip(tup,l)) == 0:
                return False
    return True

result = 0
with open("./input/p105_sets.txt", "r") as infile:
    for line in infile:
        l = [int(w) for w in line.split(",")]
        if is_special(l):
            result += sum(l)
print result
