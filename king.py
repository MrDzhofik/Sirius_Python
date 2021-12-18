s = input()
f = input()
x1 = ord(s[0]) - ord('a') + 1
y1 = int(s[1])
x2 = ord(f[0]) - ord('a') + 1
y2 = int(f[1])
if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
	print('YES')
else:
	print('NO')