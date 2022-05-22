n=int(input())
a=list(map(int,input().strip().split()))
odd=0
for i in range(n):
    if i%2==0:
        odd=odd+a[i]
print(odd)