N = int(input())
A = list(map(int, input().split()))

MaxVal = 0

for l in range(N):
    for m in range(l+1, N+1):
        x = min(A[l:m]) * (m - l)
        if x > MaxVal:
            MaxVal = x

print(MaxVal)

