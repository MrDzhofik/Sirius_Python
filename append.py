n = list(map(int, input().split()))
v = list(map(int, input().split()))
for i in range(0, len(n) - 1, 2):
	n[i] = n[i + 1]
n.insert(v[0], v[1])
print(n)