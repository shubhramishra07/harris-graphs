import numpy as np
from collections import defaultdict
from HGlist import order7, order8, order9, order10
from dataclasses import dataclass
from statistics import median

@dataclass
class Graph:
    def __init__(self, s, order):
        self.order = order
        self.size = 0
        self.g = defaultdict(lambda: [])
        self.g_matrix = np.zeros((order, order))
        edges = s.split(";")
        for edge in edges:
            verts = edge.split(",")
            self.size += 1
            verts[0] = int(verts[0])
            verts[1] = int(verts[1])
            self.g[verts[0]].append(verts[1])
            self.g[verts[1]].append(verts[0])
            self.g_matrix[verts[0]][verts[1]] = 1
            self.g_matrix[verts[1]][verts[0]] = 1
        
# A Python3 program for finding number of
# triangles in an Undirected Graph. The
# program is for adjacency matrix
# representation of the graph

# Utility function for matrix
# multiplication
def multiply(A, B, C):
    global order
    for i in range(order):
        for j in range(order):
            C[i][j] = 0
            for k in range(order):
                C[i][j] += A[i][k] * B[k][j]

# Utility function to calculate
# trace of a matrix (sum of
# diagonal elements)
def getTrace(graph):
    global order
    trace = 0
    for i in range(order):
        trace += graph[i][i]
    return trace

# Utility function for calculating
# number of triangles in graph
def triangleInGraph(graph, order):

    
    # To Store graph^2
    aux2 = [[None] * order for i in range(order)]

    # To Store graph^3
    aux3 = [[None] * order for i in range(order)]

    # Initialising aux
    # matrices with 0
    for i in range(order):
        for j in range(order):
            aux2[i][j] = aux3[i][j] = 0

    # aux2 is graph^2 now printMatrix(aux2)
    multiply(graph, graph, aux2)

    # after this multiplication aux3 is
    # graph^3 printMatrix(aux3)
    multiply(graph, aux2, aux3)

    trace = getTrace(aux3)
    return trace // 6

"""
# Driver Code

# Number of vertices in the graph
V = 4
graph = [[0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]]

print("Total number of Triangle in Graph :",
                    triangleInGraph(graph))

# This code is contributed by PranchalK
"""

for l in [(order7, 7), (order8, 8), (order9, 9), (order10, 10)]:
    num_tri = []
    print("order", l[1])
    for elem in l[0]:
        graph = Graph(elem, l[1])
        order = l[1]
        num_tri.append(triangleInGraph(graph.g_matrix, l[1]))
    print("mean number of triangles", sum(num_tri)/len(num_tri))
    print("fewest number of triangles", min(num_tri))
    print("most number of triangles", max(num_tri))
    print("median number of triangles", median(num_tri))
        
        
        
