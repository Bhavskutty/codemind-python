num=int(input())
n=len(str(num))
sq=num**2
last=sq%pow(10,n)
if last==num:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')

    