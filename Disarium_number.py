n=int(input())
m=n
s=0
def fun(d):
    sd=str(d)
    return len(sd)
while m>0:
    s+=(m%10)**fun(m)
    m=m//10
if s==n:
    print("True")
else:
    print("False")