n, k = map(int, input().strip().split(' '))
a = list(map(str, input().strip().split(' ')))
k%=n
print(" ".join(a[k:n]+a[:k]))
