n=int(input())
a=0
b=1
while(n>b):
    c=a+b
    a=b
    b=c
if a==n or b==n:
    print(True)
else:
    print(False)