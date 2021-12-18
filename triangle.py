def triangle(a, b, c):
	if a + b > c and a + c > b and b + c > a:
	    return True
	else:
	    return False

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if triangle(a,b,c) or triangle(a,b,d) \
  or triangle(a,c,d) or triangle(b,c,d):
    print("YES")
else:
    print("NO")