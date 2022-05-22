n=int(input())
a=list(map(int,input().strip().split()))
even=0
for i in range(n):
    if a[i]%2:
        even=even+a[i]
print(even)