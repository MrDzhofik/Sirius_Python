n, m = map(int, input().split())
a = [input().split() for i in range(n)]
i, j = map(int, input().split())

for b in range(n):
    a[b][i], a[b][j] = a[b][j], a[b][i]

for row in a:
	print(' '.join(row))