def move (n, start, finish):
    if n > 0:
	    tmp = 6 - start - finish
	    move(n - 1 , start, tmp)
	    print(n, start, finish)
	    move(n - 1, tmp, finish)

s = int(input())
st = int(input())
sta = int(input())
move(s, st, sta)