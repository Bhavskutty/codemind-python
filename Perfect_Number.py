n=int(input())
pfs_n=0
for i in range(1,n):
    if n%i==0:
        pfs_n+=i
p=0
if pfs_n==n:
    p+=1
if p>0:
    print("True")
else:
    print("False")