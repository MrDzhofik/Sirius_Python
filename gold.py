n, m = map(int, input().split())
a = [input().split() for i in range(n)]
x = int(input())
gold = 0

for step in range(x):
	x, y = map(int, input().split())
	gold += int(a[x - 1][y - 1])
	a[x - 1][y - 1] = 0


print(gold)