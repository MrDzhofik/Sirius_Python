def makeLevel(n):
    s = n + 2
    while n <= s:
        for i in range(1, n):
            print('*' * i)
            if i + 1 == n:
	            n += 1


def tree(n):
    makeLevel(n)



n = int(input())
tree(n)