# 211227
# 문제: 록 페스티벌 (난이도:  하, 문제 ID: FESTIVAL)
res = []
for _ in range(int(input())):
    N, L = map(int, input().split())
    costs= list(map(int, input().split()))
    minCost=sum(costs)/N
    for i in range(L,N+1): # 공연을 진행하는 일수 : i일
        for j in range(N-i): # 공연을 시작하는 날 : j번째 날
            minCost = min(minCost, sum(costs[j: j+i])/i)
    res.append(minCost)

for r in res:
    print("%.10f"%r)
