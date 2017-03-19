t = int(input())
for tt in range(0,t):
    s=input().strip()
    l=list(s)
    r=l[::-1]
    x=[abs(ord(l[i])-ord(r[i])) for i in range(0,len(s))]
    if sum(x)==0:
        if(len(x)%2==0):
            print("YES EVEN")
        else:
            print("YES EVEN")
    else:
        print("NO")
        
