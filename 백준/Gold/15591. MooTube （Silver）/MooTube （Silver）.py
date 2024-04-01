from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(n-1):
    s, e, u = map(int, input().split())
    g[s].append((e, u))
    g[e].append((s, u))


def bfs(k, st):
    q = deque()
    q.append((st, float('inf')))
    visited = [0] * (n+1)
    visited[st] = 1
    res = 0

    while q:
        v, u = q.popleft()
        for nv, nu in g[v]:
            nu = min(u, nu)
            if visited[nv] == 0 and nu >= k:
                    res += 1
                    q.append((nv,nu))
                    visited[nv] = 1
    return res



for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
