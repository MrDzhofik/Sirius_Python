n = int(input())
a = [[str((int)((i == j) + abs(i - j))) for j in range(n)] for i in range(n)]

for i in range(n):
	a[i][i] = '0'


for row in a:
	print(' '.join(row))