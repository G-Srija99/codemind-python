def reversedigit(num):
    rev=0
    while(num>0):
        s=num%10
        rev=rev*10+s
        num=num//10
    return rev
def square(num):
    return(num*num)
def adamnumber(num):
    a=square(num)
    b=square(reversedigit(num))
    if a==(reversedigit(b)):
        return True
    else:
        return False
num=int(input())
if (adamnumber(num)):
    print(True)
else:
    print(False)
    