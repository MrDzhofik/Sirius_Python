sentence = input().upper()
amount = 0
letters = []
for i in sentence:
	if sentence.count(i) > amount:
		amount = sentence.count(i)
		letters.append(i)

print(letters[-1])
print(amount)