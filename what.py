def f():
	global a
	global b
	b, c = a, b
def g():
	global a
	global d
	c = '0'
	a = d + c

a = '2'
b = '3'
c = '5'
d = '7'
f()
g()
f()
print(a + b + c + d)