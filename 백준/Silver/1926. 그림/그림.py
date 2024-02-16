from collections import deque

n, m = map(int, input().split(' '))

g =[]
for i in range (n):
    g.append(list(map(int , input().split(' '))))

v = [[0 for i in range(m)] for i in range(n)]
max_n = 0
t = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
    q = deque([(i,j)])
    if v[i][j] == 1:
        return 0
    else:
        v[i][j] = 1
    cnt = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not v[nx][ny] and g[nx][ny] == 1:
                    v[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if g[i][j] == 1 and v[i][j] == 0:
            t += 1
            max_n = max(max_n, bfs(i,j))


print(t,max_n)

