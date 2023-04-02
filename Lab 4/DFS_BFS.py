from collections import deque
import random
import matplotlib.pyplot as plt
import time
from prettytable import PrettyTable


def DFS(graph, start):
    visited = []
    stack = deque()
    stack.append(start)
    while len(stack) > 0:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            for adjacent_node in reversed(graph[current]):
                stack.append(adjacent_node)
    return visited


def BFS(graph, start):
    visited = []
    queue = []
    visited.append(start)
    queue.append(start)
    while len(queue) > 0:
        current = queue.pop(0)
        for node in graph[current]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    return visited


graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [],
    5: [6],
    6: [],
    7: [8, 9],
    8: [],
    9: [7],
    10: [11],
    11: [],
    12: [13, 14],
    13: [],
    14: [15],
    15: [],
    16: [],
    17: [18, 19],
    18: [],
    19: [20],
    20: [21],
    21: []
}

graph_2 = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [14, 15],
    4: [17, 18, 19, 21],
    5: [7, 9],
    6: [10, 11, 13],
    7: [8],
    8: [],
    9: [],
    10: [],
    11: [12],
    12: [],
    13: [],
    14: [16],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [20],
    20: [],
    21: []
}


graph_3 = {}
for i in range(1, 101):
    graph_3[i] = []
    for j in range(1, 101):
        if i != j and random.randint(0, 99) < 10:
            graph_3[i].append(j)

graph_4 = {}
for i in range(1, 101):
    graph_4[i] = []
    for j in range(1, 101):
        if i != j:
            graph_4[i].append(j)

results = []

start = time.time()
for i in range(1000):
    for j in range(1, 22):
        DFS(graph, j)
end = time.time()
results.append((end - start)/1000)

start = time.time()
for i in range(1000):
    for j in range(1, 22):
        BFS(graph, j)
end = time.time()
results.append((end - start)/1000)

start = time.time()
for i in range(1000):
    for j in range(1, 22):
        DFS(graph_2, j)
end = time.time()
results.append((end - start)/1000)

start = time.time()
for i in range(1000):
    for j in range(1, 22):
        BFS(graph_2, j)
end = time.time()
results.append((end - start)/1000)

start = time.time()
for j in range(1, 101):
    DFS(graph_3, j)
end = time.time()
results.append(end - start)

start = time.time()
for j in range(1, 101):
    BFS(graph_3, j)
end = time.time()
results.append(end - start)

start = time.time()
for j in range(1, 101):
    DFS(graph_4, j)
end = time.time()
results.append(end - start)

start = time.time()
for j in range(1, 101):
    BFS(graph_4, j)
end = time.time()
results.append(end - start)

print(results)


plt.figure(1)
plt.bar(['Disconnected Graph', 'Connected Graph'],
        [results[0], results[2]], color='green')
plt.title('DFS on graphs with 21 nodes')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(2)
plt.bar(['Disconnected Graph', 'Connected Graph'],
        [results[1], results[3]], color='blue')
plt.title('BFS on graphs with 21 nodes')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(3)
plt.bar(['Less Edges', 'Almost V^2 Edges'], [
        results[4], results[6]], color='red')
plt.title('DFS on graphs with 100 nodes')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(4)
plt.bar(['Less Edges', 'Almost V^2 Edges'], [
        results[5], results[7]], color='orange')
plt.title('BFS on graphs with 100 nodes')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(5)
plt.bar(['21 Vertices', '21 Vertices', '100 Vertices', '100 Vertices'], [
        results[0], results[2], results[4], results[6]], color='green')
plt.title('DFS on graphs')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(6)
plt.bar(['21 Vertices', '21 Vertices', '100 Vertices', '100 Vertices'], [
        results[1], results[3], results[5], results[7]], color='blue')
plt.title('BFS on graphs')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')

plt.figure(7)
plt.plot(['21 Vertices', '21 Vertices', '100 Vertices', '100 Vertices'], [
         results[0], results[2], results[4], results[6]], color='green', label='DFS')
plt.plot(['21 Vertices', '21 Vertices', '100 Vertices', '100 Vertices'], [
         results[1], results[3], results[5], results[7]], color='blue', label='BFS')
plt.title('DFS and BFS on graphs')
plt.xlabel('Graphs')
plt.ylabel('Time in seconds')
plt.legend()

plt.show()
