def linearsearch(n,arr,se):
    for i in range(n):
        if arr[i]==se:
            return True
    return False

n=int(input())
arr=list(map(int,input().split()))
se=int(input())
if(linearsearch(n,arr,se)):
    print("True")
else:
    print("False")