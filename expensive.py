n, m = map(int,input().split())
p=[list(map(int,input().split())) for i in range(n)]
a = [[0]*m for i in range(n)]
a[0][0]=p[0][0]
bbb = [[0]*(m+1) for i in range(n)]
for j in range(1, m):
	a[0][j]=a[0][j-1]+p[0][j]
for s in range(1, n):
	a[s][0]=a[s-1][0]+p[s][0]
for x in range(1, n):
	for y in range(1, m):
		a[x][y]=max(a[x-1][y],a[x][y-1])+p[x][y]

for q in range(n):
	for w in range(m):
		bbb[q][w]=a[-q-1][-w-1]
		bbb.append([0]*(m+1))

ccc=[]
i=0
j=0
nn=n-1
while i < nn:
	while j < m:
		tt=bbb[i][j]
		tt_r=bbb[i][j+1]
		tt_d=bbb[i+1][j]
		if tt_r>tt_d:
			ccc.append('R')
			j=j+1
		else:
			i=i+1
		if i>nn:
			break
		else:
			ccc.append('D')

print(a[-1][-1])
for ii in range(len(ccc)):
	print(ccc[-ii-1], end = ' ')