t=int(input())
for i in range(t):
    n = int(input()) 
    a = n
    while True:
        is_prime = True
        for i in range(2,int(a**0.5)+1):
            if a % i == 0:
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            a+=1
    b = n
    while True:
        is_prime = True
        for i in range(2,int(b**0.5)+1):
            if b % i == 0:
                is_prime = False
                break
        if is_prime == True:
            break
        else:
            b-=1
    d1=b-n
    d2=n-a
    if  d1<d2:
        print(a)
    elif d1==d2 and a<b:
        print(a)
    else:
        print(b)
    