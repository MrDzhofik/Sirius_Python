n = int(input())
A = [[4] * i + [0] + [1] * (n - 2 * (i + 1)) + [0] + [2] * i if i + 1 <= n // 2 else [4] * (n - i - 1) + [0] + [3] * (n - 2 * (n - i)) + [0] + [2] * (n - i - 1) for i in range(n)]
for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()