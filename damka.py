def Ssposob(x,y,N):
    if y==8:
        return N
    if x==1:
        return Ssposob(2, y+1, N)
    if x==8:
        return Ssposob(7, y+1, N)
    return (Ssposob(x+1, y+1, N) + Ssposob(x-1, y+1, N))
n, m = map(int, input().split())
print(Ssposob(n,m,1))