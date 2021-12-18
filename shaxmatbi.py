n, m = map(int, input().split())
A = [[(int)(1 * ((i - j) % 2) == 0) for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        print(A[i][j], end = ' ')
    print()