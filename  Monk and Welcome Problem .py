n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(*[a[i]+b[i] for i in range(0,n)])
