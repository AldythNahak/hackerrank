#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque as deque_1
from collections import deque as deque_2

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
def buildTree(n, edges):
    nodes = {i: TreeNode(i) for i in range(1, n + 1)}
    for h, b in edges:
        nodes[h].neighbors.append(nodes[h])
        nodes[b].neighbors.append(nodes[b])
    
    return nodes

def bfs_object(n, m, edges, s):
    tree = buildTree(n, edges)
    visited = set()
    distance = {i: -1 for i in range(1, n + 1)}
    q = deque_2([tree[s]])
    distance[s] = 0
    visited.add(s)

    while q:
        node = q.popleft()
        for neighbor in node.neighbors:
            if neighbor.value not in visited:
                visited.add(neighbor.value)
                distance[neighbor.value] = distance[node.value] + 6
                q.append(neighbor)
                
    return [distance[i] for i in range(1, n + 1) if i != s]


def bfs(n, m, edges, s):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    distances = [-1] * (n + 1)
    visited = [False] * (n + 1)
    distances[s] = 0
    visited[s] = True
    
    queue = deque_1([s])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[node] + 6
                queue.append(neighbor)

    return [distances[i] for i in range(1, n + 1) if i != s]
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     m = int(first_multiple_input[1])

    #     edges = []

    #     for _ in range(m):
    #         edges.append(list(map(int, input().rstrip().split())))

    #     s = int(input().strip())

    #     result = bfs(n, m, edges, s)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
    print(bfs_object(5, 3, [[1,2], [1,3], [3,4]], 1))
    print(bfs(5, 3, [[1,2], [1,3], [3,4]], 1))
