n=int(input())
l=[int(i) for i in input().split()]
ans=1
for i in range(0,n):
    ans=(ans*l[i])%1000000007
print(ans)
