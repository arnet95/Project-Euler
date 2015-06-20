#Euler 81
#Create matrix of floats
matrix = []
infile = open("p081_matrix.txt","r")
for line in infile:
    matrix.append(line.split(","))
infile.close()

#Create matrix of integers
a_matrix = []
for i in xrange(len(matrix)):
    a_matrix.append([])
    for j in matrix[i]:
        a_matrix[i].append(int(j))

min_matrix = []
for i in xrange(len(matrix)):
    min_matrix.append([])
    for j in matrix[i]:
        min_matrix[i].append(-1)

#Populate first row
min_matrix[0][0] = a_matrix[0][0]
for j in xrange(len(matrix[0])):
    if min_matrix[0][j] == -1:
        min_matrix[0][j] = min_matrix[0][j-1] + a_matrix[0][j]

#Populate first column
for i in xrange(80):
    if min_matrix[i][0] == -1:
        min_matrix[i][0] = min_matrix[i-1][0] + a_matrix[i][0]

#Populate rest of table
for i in xrange(1,80):
    for j in xrange(1,80):
        min_matrix[i][j] = min(min_matrix[i][j-1], min_matrix[i-1][j]) + a_matrix[i][j]

print min_matrix[-1][-1]
