n, m = map(int, input().split())
p = [list(map(int, input().split())) for i in range(n)]
a = [[0] * m for i in range(n)]
a[0][0] = p[0][0]
for j in range(1, m):
    a[0][j] = a[0][j - 1] + p[0][j]
for i in range(1, n):
    a[i][0] = a[i - 1][0] + p[i][0]
for i in range(1, n):
    for j in range(1, m):
        a[i][j] = min(a[i][j - 1],a[i - 1][j]) + p[i][j]

print(a[n - 1][m - 1])