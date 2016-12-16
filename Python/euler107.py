#Project Euler 107: Minimal network

#This problem is essentially about finding a minimal spanning tree.
#To solve it, we implement Prim's algorithm, and get the answer quite easily.

with open("../input/p107_network.txt", "r") as infile:
    matrix = [line.split(',') for line in infile]

graph = {i: [((i, j), int(matrix[i][j])) for j in xrange(40) if '-' not in matrix[i][j]] for i in xrange(40)}

def sum_of_graph(graph):
    return sum(elem[1] for key in graph for elem in graph[key])/2

def prim(input_graph):
    graph_vertices = [key for key in input_graph]
    tree = {graph_vertices[0]: []}
    current = graph_vertices[0]
    tree_vertices = [current]
    edges = input_graph[current][:]
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
        edges += input_graph[node[0][1]]
        #Remove unwanted edges
        edges = filter(lambda x: x[0][1] not in tree_vertices, edges)
    return tree

print sum_of_graph(graph) - sum_of_graph(prim(graph))
