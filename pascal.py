n, m = map(int, input().split())

pascal = [[1] * n for i in range(m)]

for i in range(1, m):
    for j in range(1, n):
    	pascal[i][j] = pascal[i-1][j] + pascal[i][j-1]

for i in range(len(pascal)):
    print(*pascal[i])