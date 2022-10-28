n=int(input())
lst=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(lst)):
    if lst[i]%2==0:
        sum1+=lst[i]
    else:
        sum2+=lst[i]
x=abs(sum1-sum2)
print(x)