array = list(map(int, input().split()))
for i in range(0, len(array)):
	if (array[i] > 0 and array[i + 1] > 0) or (array[i] < 0 and array[i + 1] < 0):
		print(array[i], array[i + 1])
		break