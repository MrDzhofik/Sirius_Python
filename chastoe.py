array = [int(s) for s in input().split()]
minimum = 1
number = 0
for i in range(0, len(array)):
	if array.count(array[i]) >= minimum:
		minimum = array.count(array[i])
		number = array[i]
print(number)