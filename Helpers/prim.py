#Prim's algorithm

#assume given graph



graph2 = {'a': [(('a', 'b'), 1), (('a', 'c'), 2), (('a', 'd'), 3)],
        'b': [(('b', 'a'), 1), (('b', 'c'), 4), (('b', 'd'), 5)],
        'c': [(('c', 'a'), 2), (('c', 'b'), 4), (('c', 'd'), 6)],
        'd': [(('d', 'a'), 3), (('d', 'b'), 5), (('d', 'c'), 6)]}

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'

graph = {a: [((a, b), 16), ((a, c), 12), ((a, d), 21)],
        b: [((b, a), 16), ((b, d), 17), ((b, e), 20)],
        c: [((c, a), 12), ((c, d), 28), ((c, f), 31)],
        d: [((d, a), 21), ((d, b), 17), ((d, c), 28), ((d, e), 18), ((d, f), 19), ((d, g), 23)],
        e: [((e, b), 20), ((e, d), 18), ((e, g), 11)],
        f: [((f, c), 31), ((f, d), 19), ((f, g), 27)],
        g: [((g, d), 23), ((g, e), 11), ((g, f), 27)]}




def prim(graph):
    graph_vertices = [key for key in graph]
    tree = {graph_vertices[0]: []}
    current = graph_vertices[0]
    tree_vertices = [current]
    edges = graph[current]
    while len(tree_vertices) < len(graph_vertices):
        node = min(edges, key=lambda x: x[1])
        edges.remove(node)
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
        edges = edges + graph[node[0][1]]
        #Remove unwanted edges
        new_edges = []
        for edge in edges:
            if edge[0][1] not in tree_vertices:
                new_edges.append(edge)
        edges = new_edges[:]
    
    return tree

#print prim(graph)

def sum_of_graph(graph):
    s = 0
    for key in graph:
        for elem in graph[key]:
            s += elem[1]
    return s/2

print sum_of_graph(graph)
print sum_of_graph(prim(graph))