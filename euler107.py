#Euler 107

matrix = []
infile = open("p107_network.txt", "r")
for line in infile:
    matrix.append(line.split(','))
infile.close()

graph = {}
for i in xrange(40):
    graph[i] = []
    for j in xrange(40):
        x = matrix[i][j]
        if '-' not in x:
           graph[i].append(((i, j), int(matrix[i][j])))

def sum_of_graph(graph):
    return sum(elem[1] for key in graph for elem in graph[key])/2

def prim(in_graph):
    graph_vertices = [key for key in in_graph]
    tree = {graph_vertices[0]: []}
    current = graph_vertices[0]
    tree_vertices = [current]
    edges = in_graph[current][:]
    while len(tree_vertices) < len(graph_vertices):
        node = min(edges, key=lambda x: x[1])
        #Adding nodes to tree
        if node[0][0] in tree:
            tree[node[0][0]].append(node)
        else:
            tree[node[0][0]] = [node]
        if node[0][1] in tree:
            tree[node[0][1]].append(((node[0][1], node[0][0]), node[1]))
        else:
            tree[node[0][1]] = [((node[0][1], node[0][0]), node[1])]
        tree_vertices.append(node[0][1])
        edges = edges + in_graph[node[0][1]]
        #Remove unwanted edges
        edges = filter(lambda x: x[0][1] not in tree_vertices, edges)
    return tree

print sum_of_graph(graph) - sum_of_graph(prim(graph))
