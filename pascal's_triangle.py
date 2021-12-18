n, m = map(int, input().split())
a = [['1'] * n for i in range(n)]

for row in range(1, n):
	for elem in range(1, n):
	    a[row][elem] = str(int(a[row][elem - 1]) + int(a[row -1][elem]))

for number in a:
    if n == 1 and m == 1:
	    number = '1'
    print(' '.join(number))