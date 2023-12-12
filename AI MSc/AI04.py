# Write a program to count the total number of goal states.


# Function to count the number of nodes # with maximum connections
def get(graph):
    # Stores the number of connections # of each node
    v = []

    # Stores the maximum connections
    mx = -1
    for arr in graph.values():
        v.append(len(arr))
        mx = max(mx, (len(arr)))

    # Resultant count
    cnt = 0
    for i in v:
        if i == mx:
            cnt += 1
    print(cnt)


# Drive Code
graph = {}

nodes = 10
edges = 13
for i in range(1, nodes + 1):
    graph[i] = []

# 1
graph[1].append(4)
graph[4].append(1)

# 2
graph[2].append(3)
graph[3].append(2)

# 3
graph[4].append(5)
graph[5].append(4)

# 4
graph[3].append(9)
graph[9].append(3)

# 5
graph[6].append(9)
graph[9].append(6)

# 6
graph[3].append(8)
graph[8].append(3)

# 7
graph[10].append(4)
graph[4].append(10)

# 8
graph[2].append(7)
graph[7].append(2)

# 9
graph[3].append(6)
graph[6].append(3)

# 10
graph[2].append(8)
graph[8].append(2)

# 11
graph[9].append(2)
graph[2].append(9)

# 12
graph[1].append(10)
graph[10].append(1)

# 13
graph[9].append(10)
graph[10].append(9)

get(graph)
