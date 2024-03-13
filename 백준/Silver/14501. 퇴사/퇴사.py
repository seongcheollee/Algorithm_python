import copy
n = int(input())

t = []
p = []

for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

res = []
for i in range(n):
    if t[i] + i <= n:
        res.append(p[i])
    else:
        res.append(0)

for i in range(n):
    for j in range(i+1,n):
        # 선택 가능 여부 계산
        if i + t[i] > j:
            continue
        if j + t[j] > n:
            continue
        res[j] = max(res[i] + p[j], res[j])

print(max(res))

