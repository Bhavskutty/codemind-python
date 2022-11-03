def sd(n):
    t=n
    while n>0:
        r=n%10
        if r==0 or t%r!=0:
            return False
        n=n//10
    return True
x=int(input())
y=int(input())
for i in range(x,y+1):
    if sd(i)==True:
        print(i,end=' ')
    
        

