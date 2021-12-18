n = list(map(int, input().split()))
k = int(input())
n[k], n[-1] = n[-1], n[k]
n.pop(k)
for elem in n:
	print(elem, end=' ')