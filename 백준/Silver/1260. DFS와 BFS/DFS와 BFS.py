import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)

n, m, start = map(int, input().split(' '))
g = [[] for i in range(n+1)]


for i in range(1,m+1):
    a, b = map(int, input().split(' '))
    g[a].append(b)
    g[b].append(a)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for i in range(1,n+1):
    g[i].sort()

def dfs(s):
    print(s, end=" ")
    visited_dfs[s] = True

    for i in g[s]:
        if not visited_dfs[i]:
            dfs(i)                

def bfs(s):
    visited_bfs[s] = True
    q = deque([s])
    
    while q:
        p = q.popleft()
        print(p, end=" ")
        for i in g[p]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] =True


dfs(start)
print('')
bfs(start)