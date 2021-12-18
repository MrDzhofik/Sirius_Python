n = int(input())
a =[list(map(int, input().split())) for i in range(n)]
for i in range(n):
    a[i][i], a[n - 1 - i][i] = a[n - 1 - i][i], a[i][i]
 
for row in a:
	print(*row)