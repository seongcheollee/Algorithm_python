from collections import deque

gear = []

for i in range(4):
    gear.append(input())

k = int(input())

def rotate(i, d):
    # 시계방향
    if d == 1:
        gear[i] = gear[i][7]+gear[i][:7]
    # 시계 반대
    else:
        gear[i] = gear[i][1:] + gear[i][0]

def dfs(s,d):

    v[s] = 1
    if s < 0 or s >= 4:
        return
    temp = gear[s]
    rotate(s,d)

    if 0 <= s-1 and v[s-1] == 0:
        if gear[s - 1][2] != temp[6]:
            dfs(s-1,-d)

    if s+1 < 4 and v[s+1] == 0:
        if gear[s+1][6] != temp[2]:
            dfs(s+1,-d)


# 맞 닿는곳 2(3)번 6(7)번
for i in range(k):
    n, d = map(int,input().split(' '))
    v = [0] * 4
    dfs(n-1,d)

res = 0
res_c = [1,2,4,8]
for i in range(4):
    if gear[i][0] == '1':
        res += res_c[i]

print(res)