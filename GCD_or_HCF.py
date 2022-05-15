n,m=map(int,input().split())
i=1
while(i<=n and i<=m):
    if(n%i==0 and m%i==0):
        val=i
    i=i+1
print(val)