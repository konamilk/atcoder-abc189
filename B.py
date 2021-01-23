N, X = map(int, input().split())
V = []
P = []

for i in range(N):
    vn, pn = map(int, input().split())
    V.append(vn)
    P.append(pn)

# print(N, X, V, P)

sum_alcohole = 0
hai = 0
flg = False

for i in range(N):
    alcohole = V[i] * P[i] / 100
    sum_alcohole += alcohole
    if sum_alcohole > X:
        hai = i + 1
        flg = True
        break

if flg:
    print(hai)

else:
    print('-1')


