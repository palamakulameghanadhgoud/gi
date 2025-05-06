# Initialize global variables
visited = []
queue = []

def bfs(s):
    # Explore all neighbors of the current node
    for i in range(n):
        if graph[s][i] == 1 and visited[i] == 0:
            queue.append(i)
    
    # Visit next node in the queue
    if queue:
        next_node = queue.pop(0)
        visited[next_node] = 1
        bfs(next_node)

# Main program
n = int(input("Enter the number of vertices: "))
graph = []

# Initialize graph (adjacency matrix), visited list and queue
visited = [0 for _ in range(n)]
queue = []

print("Enter the adjacency matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

s = int(input("Enter the source vertex: "))
visited[s] = 1
bfs(s)

print("Visited vertices in BFS order:")
for i in range(n):
    if visited[i]:
        print(i, end=' ')
