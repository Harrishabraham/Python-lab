n = int(input("Enter number of users: "))
graph = [[] for _ in range(n)]
e = int(input("Enter number of friendships: "))
print("Enter the friendships:")
for i in range(e):
    u = int(input("Enter first user: "))
    v = int(input("Enter second user: "))
    graph[u].append(v)
    graph[v].append(u)
print("Social Network:")
for i in range(n):
    print(i, "->", graph[i])
user = int(input("Enter user to find friends: "))
print("Friends of user", user, ":", graph[user])
def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    visited[start] = True
    queue.append(start)
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current)
        for friend in graph[current]:
            if not visited[friend]:
                visited[friend] = True
                queue.append(friend)
    return result
def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    for friend in graph[start]:
        if not visited[friend]:
            dfs(graph, friend, visited, result)
start = int(input("Enter starting user for BFS and DFS: "))
bfs_result = bfs(graph, start)
print("BFS Traversal:")
print(bfs_result)
visited = [False] * n
dfs_result = []
dfs(graph, start, visited, dfs_result)
print("DFS Traversal:")
print(dfs_result)
