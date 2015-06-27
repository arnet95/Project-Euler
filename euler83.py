#Euler 83

matrix = []
with open("p082_matrix.txt","r") as infile:
    for line in infile:
        matrix.append(line.split(","))

cost_matrix = []
for i in xrange(len(matrix)):
    cost_matrix.append([])
    for j in matrix[i]:
        cost_matrix[i].append(int(j))

def dijkstra(graph, begin, end, max_val=10**8):
    values = {node: max_val for node in graph}
    values[begin] = 0
    current = begin
    unvisited = [node for node in graph]
    while end in unvisited:
        for node in graph[current]:
            values[node] = min(values[node], values[current] + graph[current][node])
        unvisited.remove(current)
        try:
            current = min(unvisited, key=lambda x: values[x])
        except:
            break
    return values[end]

def matrix_to_graph(matrix):
    graph = {}
    c = len(matrix[0])
    l = len(matrix)
    #First row
    graph[(0, 0)] = {(0,1):matrix[0][1] , (1,0):matrix[1][0]}
    for j in xrange(1, c-1):
        graph[(0, j)] = {(0, j-1):matrix[0][j-1], (0, j+1):matrix[0][j+1], (1, j):matrix[1][j]}
    graph[(0, c-1)] = {(0, c-2): matrix[0][c-2], (1, c-1):matrix[1][c-1]}
    for i in xrange(1, l-1):
        graph[(i, 0)] = {(i-1, 0):matrix[i-1][0] , (i, 1):matrix[i][1] , (i+1, 0):matrix[i+1][0]}
        for j in xrange(1, c-1):
            graph[(i, j)] = {(i-1, j):matrix[i-1][j], (i+1, j):matrix[i+1][j], (i, j-1):matrix[i][j-1], (i, j+1):matrix[i][j+1]}
        graph[(i, c-1)] = {(i-1, c-1):matrix[i-1][c-1] , (i, c-2):matrix[i][c-2] , (i+1, c-1):matrix[i+1][c-1]}
    graph[l-1, 0] = {(l-2, 0): matrix[l-2][0], (l-1, 1): matrix[l-1][1]}
    for j in xrange(1, c-1):
        graph[(l-1, j)] = {(l-1, j-1): matrix[l-1][j-1], (l-1, j+1): matrix[l-1][j+1], (l-2, j): matrix[l-2][j]}
    graph[(l-1, c-1)] = {(l-2, c-1): matrix[l-2][c-1], (l-1, c-2): matrix[l-1][c-2]}
    return graph

print cost_matrix[0][0] + dijkstra(matrix_to_graph(cost_matrix), (0,0), (len(matrix)-1,len(matrix[0])-1))
