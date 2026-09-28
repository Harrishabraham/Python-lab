n = int(input("Enter the total number of users: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)
list1 = []
for i in range(n):
    list1.append([])
e = int(input("Enter the number of connections: "))
print("Enter the connections:")
for i in range(e):
    u = int(input("Enter first user: "))
    v = int(input("Enter second user: "))
    matrix[u][v] = 1
    matrix[v][u] = 1
    list1[u].append(v)
    list1[v].append(u)
print("\nAdjacency Matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print("\nAdjacency List:")
for i in range(n):
    print(i, "->", end=" ")
    for j in list1[i]:
        print(j, end=" ")
    print()
u = int(input("\nEnter first user: "))
v = int(input("Enter second user: "))
if matrix[u][v] == 1:
    print("Using Adjacency Matrix: Users are directly connected")
else:
    print("Using Adjacency Matrix: Users are not directly connected")
if v in list1[u]:
    print("Using Adjacency List: Users are directly connected")
else:
    print("Using Adjacency List: Users are not directly connected")
