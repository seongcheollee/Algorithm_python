import sys
from collections import deque
input = sys.stdin.readline

# 건물 층 수, 현재 층 수, 목표 층 수, up 개수, down 개수
F, S, G, U, D = map(int,input().split(' '))
g = [0] * (F+1)

def bfs(s):
    q = deque([s])
    dx = [U,-D]
    g[s] = 1

    while q:
        x = q.popleft()

        if x == G:
            return g[x] -1

        for i in range(2):
            nx = x + dx[i]

            if 0 < nx <= F and g[nx] == 0:
                g[nx] = g[x]+1
                q.append(nx)


    return 'use the stairs'

res = bfs(S)
print(res)
