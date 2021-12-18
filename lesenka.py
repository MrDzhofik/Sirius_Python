def kol_les(k,n):
    ans=0
    if n==0:
        return ans+1
    elif k<n:
        for i in range(k+1,n+1):
            ans+=kol_les(i, n-i)
        return ans
    else:
        return ans
n=int(input())
print(kol_les(0,n))