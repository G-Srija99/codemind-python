n=int(input())
a=list(map(int,input().strip().split()))
even=0
odd=0
for i in range(0,n,1):
    if i%2==0:
        even=abs(even+a[i])
    else:
        odd=abs(odd+a[i])
s=even-odd
print(s)
        