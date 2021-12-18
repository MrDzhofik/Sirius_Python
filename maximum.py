n, m = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
max_i, max_j = 0, 0
current_max = a[0][0]


for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            current_max = a[i][j]
            max_i, max_j = i, j


print(max_i, max_j)
