t=int(input())
for tt in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split()]
    mn=min(a)
    c=0
    for i in range(0,len(a)):
        if a[i]==mn:
            c+=1
    if c%2!=0:
        print('Lucky')
    else:
        print('Unlucky')
