#Euler 82

matrix = []
with open("./input/p082_matrix.txt","r") as infile:
    for line in infile:
        matrix.append(line.split(","))

cost_matrix = [[int(j) for j in matrix[i]] for i in xrange(80)]

min_matrix = [[10**10 for _ in matrix[i]] for i in xrange(80)]

#Populate first column
for i in xrange(len(matrix)):
    min_matrix[i][0] = cost_matrix[i][0]

for i in xrange(1, len(matrix)):
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
    for j in xrange(1, len(matrix[i])-1):
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

n = 10**10
for i in min_matrix:
    n = min(i[-1], n)
print n
#for i in xrange(len(min_matrix)):
#    print min_matrix[i][0], min_matrix[i][1], min_matrix[i][2], "     ", cost_matrix[i][0], cost_matrix[i][1], cost_matrix[i][2]
