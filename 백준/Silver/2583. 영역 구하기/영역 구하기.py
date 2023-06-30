
from collections import deque
import sys
sys.setrecursionlimit(10**9)

m,n,k = map(int, input().split(' '))
g = [[0]* n for i in range(m)]
cnt = 0

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split(' '))
    for j in range(y1,y2):
        for l in range(x1,x2):
            g[j][l] = 1

def dfs(x,y):
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1]
    global cnt
    if g[x][y] == 0:
        g[x][y] = 1

    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n): 
            if g[nx][ny] == 0:
                g[nx][y] = 1
                cnt +=1
                dfs(nx,ny)
    
res = []
for i in range(m):
    for j in range(n):
        cnt = 0
        if g[i][j] == 0:
            cnt +=1
            dfs(i,j)
            res.append(cnt)

res.sort()

print(len(res))
for i in res:
    print(i, end=' ')
            