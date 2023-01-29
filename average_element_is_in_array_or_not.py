def average(n,lst):
    for i in range(n):
        avg=sum(lst)//n
        if lst[i]==avg:
            return True
    return False
n=int(input())
lst=list(map(int,input().split()))
if(average(n,lst)):
    print('True')
else:
    print('False')