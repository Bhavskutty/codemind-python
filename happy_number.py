n=int(input())
y=n
def fun(n):
    s=0
    while n>0:
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
while y!=1 and y!=4:
    y=fun(y)
if y==1:
    print("True")
else:
    print("False")