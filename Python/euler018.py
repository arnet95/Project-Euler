#Project Euler 18: Maximal path sum I

with open("../input/problem18.txt", "r") as infile:
    float_cost = [line.split() for line in infile]

int_cost = [[int(float_cost[i][j]) for j in xrange(len(float_cost[i]))] for i in xrange(len(float_cost))]
max_cost = [[0 for j in xrange(len(float_cost[i]))] for i in xrange(len(float_cost))]

max_cost[0][0] = actual_cost[0][0]
for i in xrange(1, len(actual_cost)):
    max_cost[i][0] = actual_cost[i][0] + max_cost[i-1][0]
    max_cost[i][-1] = actual_cost[i][-1] + max_cost[i-1][-1]

for i in xrange(2,len(actual_cost)):
    for j in xrange(1, i):
        max_cost[i][j] = max(max_cost[i-1][j-1], max_cost[i-1][j]) + actual_cost[i][j]

print max(max_cost[-1])

#The solution to this problem is exactly the same as for Problem 61, so the
#comments there apply for this problem as well.
