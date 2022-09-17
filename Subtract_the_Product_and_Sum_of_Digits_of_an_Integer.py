n=int(input())
s=0
p=1
q=0
while n>0:
    r=n%10
    p*=r
    s+=r
    q=p-s
    n=n//10
print(q)
    