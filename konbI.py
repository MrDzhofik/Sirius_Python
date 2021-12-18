ki = int(input())
kj = int(input())
b = [['.'] * 12 for i in range(12)]
moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
ki += 1
kj += 1
for di,dj in moves:
    i = ki + di
    j = kj + dj
    b[i][j] = '*'
b[ki][kj] = 'K'
for row in b[2:-2]:
    print(' '.join(row[2:-2]))