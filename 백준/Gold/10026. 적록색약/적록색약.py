from collections import deque

n = int(input())
g = [list(input()) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
v = [[0] * n for _ in range(n)]

def bfs(i,j):

    q = deque([(i,j)])
    v[i][j] = 1
    while q:
        x , y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if g[x][y] == g[nx][ny] and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append((nx,ny))

cnt = 0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            bfs(i,j)
            cnt += 1

n_cnt = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == 'G':
            g[i][j] =  'R'

v = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            bfs(i,j)
            n_cnt += 1

print(cnt, n_cnt)