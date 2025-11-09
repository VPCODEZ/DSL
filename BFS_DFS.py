from collections import deque

# ----- Input -----
n = int(input("Enter number of locations: "))
locations = [input(f"Enter name of location {i+1}: ") for i in range(n)]

# Initialize adjacency structures
adj_matrix = [[0]*n for _ in range(n)]
adj_list = {loc: [] for loc in locations}

# Enter connections
e = int(input("Enter number of routes (edges): "))
for _ in range(e):
    u = input("From: ")
    v = input("To: ")
    i, j = locations.index(u), locations.index(v)
    adj_matrix[i][j] = adj_matrix[j][i] = 1  # undirected
    adj_list[u].append(v)
    adj_list[v].append(u)

# ----- DFS using adjacency matrix -----
visited = [False]*n
def dfs(v):
    visited[v] = True
    print(locations[v], end=" ")
    for i in range(n):
        if adj_matrix[v][i] == 1 and not visited[i]:
            dfs(i)

# ----- BFS using adjacency list -----
def bfs(start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for nei in adj_list[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

# ----- Run Traversals -----
start = input("Enter starting location: ")
print("\nDFS (Adjacency Matrix):")
dfs(locations.index(start))

print("\nBFS (Adjacency List):")
bfs(start)
