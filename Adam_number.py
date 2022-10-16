n=int(input())
p=n*n
rev1=0
rev2=0
while n>0:
    r=n%10
    rev1=rev1*10+r
    n=n//10
sq=rev1*rev1
while sq>0:
    r1=sq%10
    rev2=rev2*10+r1
    sq=sq//10
if p==rev2:
    print("True")
else:
    print("False")