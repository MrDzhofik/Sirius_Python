def func(number, scale):
	if number < scale:
		return str(number)
	return func(number // scale, scale) + str(number % scale)
     
     
s = int(input())
n = int(input())
print(func(n, s))