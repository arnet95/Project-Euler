#Project Euler 81: Path sum: two ways

#Create matrix of strings of numbers
matrix = []
infile = open("../input/p081_matrix.txt","r")
for line in infile:
    matrix.append(line.split(","))
infile.close()

#Create matrix of integers
int_matrix = [[int(j) for j in matrix[i]] for i in xrange(80)]

#We solve this problem by dynamically building up a table of the minimal cost
#needed to reach that position. Since the only allowed moves are right and down,
#the value in the minimal cost matrix is given by the values in the minimal cost
#matrix above and to the left of a given point.
#So we have (i, j) is given by min((i-1, j), (i, j-1)) + the value in the input
#matrix in (i, j). After we've populated the entire minimal cost matrix, we can
#read off the value in the lower right corner. This gives the answer in ~10 ms.

#Create minimal cost matrix
min_matrix = [[-1 for _ in matrix[i]] for i in xrange(80)]

#Populate first row and column
min_matrix[0][0] = int_matrix[0][0]
for j in xrange(1, 80):
    min_matrix[0][j] = min_matrix[0][j-1] + int_matrix[0][j]
for i in xrange(1, 80):
    min_matrix[i][0] = min_matrix[i-1][0] + int_matrix[i][0]

#Populate rest of table
for i in xrange(1, 80):
    for j in xrange(1, 80):
        min_matrix[i][j] = min(min_matrix[i][j-1], min_matrix[i-1][j]) + int_matrix[i][j]

print min_matrix[-1][-1]
