n=int(input())
s=""
while n>0:
    r=n%10
    s=s+str(r)
    n=n//10
print(max(s))