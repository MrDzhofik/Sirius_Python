n =  int(input())
a = [input().split() for i in range(n)]
ans = "YES"


for i in range(n):
	for j in range(i + 1, n):
		if a[i][j] != a[j][i]:
		    ans = "NO"

print(ans)