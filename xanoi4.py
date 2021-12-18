def f(n, x, y):
    if n > 0:
        f(n - 1, x, 6 - x - y)
        print(n, x, y)
        f(n - 1, 6 - x - y, y)
 
 
def sortF(n, x, y):
    if n > 0:
        f(n - 1, x, 6 - x - y)
        print(n, x, y)
        if n > 3:
            f(n - 3, 6 - x - y, x)
        if n > 2:
            print(n - 2, 6 - x - y, y)
        if n > 3:
            sortF(n - 3, x, 6 - x - y)
 
 
n = int(input())
if n % 2 == 0:
    sortF(n, 1, 3)
else:
    sortF(n, 1, 2)