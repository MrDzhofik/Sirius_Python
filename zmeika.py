n, m = map(int, input().split())
a = [[str(1 + j + i * m) for j in range(m)] for i in range(n)]
for i in range(1, n, 2):
    a[i] = a[i][::-1]
for row in a:
    print(' '.join(row))
