#Euler 67
from time import time

float_cost = []
with open("p067_triangle.txt", "r") as infile:
    for line in infile:
        float_cost.append(line.split())

actual_cost = []
max_cost = []
for i in xrange(len(float_cost)):
    max_cost.append([])
    actual_cost.append([])
    for j in xrange(len(float_cost[i])):
        actual_cost[i].append(int(float_cost[i][j]))
        max_cost[i].append(0)

max_cost[0][0] = actual_cost[0][0]
for i in xrange(1, len(actual_cost)):
    max_cost[i][0] = actual_cost[i][0] + max_cost[i-1][0]
    max_cost[i][-1] = actual_cost[i][-1] + max_cost[i-1][-1]

for i in xrange(2,len(actual_cost)):
    for j in xrange(1, i):
        max_cost[i][j] = max(max_cost[i-1][j-1], max_cost[i-1][j]) + actual_cost[i][j]

print max(max_cost[-1])