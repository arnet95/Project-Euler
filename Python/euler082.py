#Project Euler 82: Path sum: three ways

matrix = []
with open("./input/p082_matrix.txt","r") as infile:
    for line in infile:
        matrix.append(line.split(","))

cost_matrix = [[int(j) for j in matrix[i]] for i in xrange(80)]
min_matrix = [[10**10 for _ in matrix[i]] for i in xrange(80)]

#Populate first column
for i in xrange(80):
    min_matrix[i][0] = cost_matrix[i][0]

for i in xrange(1, 80):
    #Populate the columns, one by one
    #min_matrix[0][i]
    guess = min_matrix[0][i-1]
    s = 0
    k = 1
    while s < guess:
        s += cost_matrix[k][i]
        guess = min(guess, s + min_matrix[k][i-1])
        k += 1
    min_matrix[0][i] = guess + cost_matrix[0][i]
    #For the rest of them
    for j in xrange(1, 79):
        guess = min(min_matrix[j][i-1], min_matrix[j-1][i])
        s = 0
        k = j+1
        while s < guess:
            try:
                s += cost_matrix[k][i]
                guess = min(guess, s + min_matrix[k][i-1])
                k += 1
            except:
                break
        min_matrix[j][i] = guess + cost_matrix[j][i]
    #min_matrix[i][-1] - Simple case
    min_matrix[-1][i] = min(min_matrix[-2][i], min_matrix[-1][i-1]) + cost_matrix[-1][i]

#We do this in a similar way to Problem 81, by building up a minimal matrix.
#We note that the minimal matrix equals the cost matrix for the first column.
#For any other column, we go from top to bottom. We try the ones to the left and
#the ones above, and try to create routes from below for as long as we can, and
#then we take the minimum of all of these.

print min(min_matrix, key=lambda x: x[-1])[-1]
#In the end, we read off the minimum of the last column with a nice little lambda.
