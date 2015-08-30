#Project Euler 67: Maximum path sum II

with open("../input/p067_triangle.txt", "r") as infile:
    float_cost = [line.split() for line in infile]

int_cost = [[int(float_cost[i][j]) for j in xrange(len(float_cost[i]))] for i in xrange(len(float_cost))]
max_cost = [[0 for j in xrange(len(float_cost[i]))] for i in xrange(len(float_cost))]

max_cost[0][0] = int_cost[0][0]
for i in xrange(1, len(int_cost)):
    max_cost[i][0] = int_cost[i][0] + max_cost[i-1][0]
    max_cost[i][-1] = int_cost[i][-1] + max_cost[i-1][-1]

for i in xrange(2,len(int_cost)):
    for j in xrange(1, i):
        max_cost[i][j] = max(max_cost[i-1][j-1], max_cost[i-1][j]) + int_cost[i][j]

print max(max_cost[-1])

#We solve this by dynamic programming, by building up a table of the maximal cost
#achievable to reach a given position. We let [i][j] denote the j'th number in the i'th row.
#Indexed from 0, of course. The important insight here is that the maximal cost
#to reach a position is determined by the two adjacent positions above.
#(Or by the single position above, in the (literal) edge cases.)
#Once this is done, we read off the maximal value in the last row, in order to
#get the result.
