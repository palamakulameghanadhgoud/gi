def dfs(i):
    print(i, end=' ')
    visited[i] = True
    for j in range(n):
        if not visited[j] and graph[i][j] == 1:
            dfs(j)

# Read number of vertices
n = int(input("Enter number of vertices: "))

# Initialize adjacency matrix
graph = []

print("Enter adjacency matrix of the graph row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Initialize visited list
visited = [False] * n

# Read source vertex
s = int(input(f"Enter source vertex (0 to {n - 1}): "))

print(f"DFS traversal starting from vertex {s}:")
dfs(s)
