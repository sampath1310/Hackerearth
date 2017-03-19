for _ in range(int(input())):
        N,K=map(int,input().split())
        arr=list(input().split())
        K%=N
        print(" ".join(arr[N-K:N]+arr[:N-K]))
