from collections import deque
import sys
input = sys.stdin.readline

n , m = map(int, input().split(' '))
g = []
for i in range(n):
    g.append(list(map(int , input().split(' '))))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def melting(x,y):
    v[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if v[nx][ny] == 0 and g[nx][ny] ==0:
                if g[x][y] > 0:
                    g[x][y] -= 1
def bfs(x,y):

    q = deque([(x,y)])
    v[x][y] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0:
                if g[nx][ny]:
                    q.append((nx,ny))
                    v[nx][ny] = 1

    return 1


ans = 0

while True:

    cnt = 0
    v = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j]:
                melting(i,j)

    v = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j] and v[i][j] == 0:
                cnt += bfs(i, j)

    ans += 1

    if cnt >= 2:
        break

    if not cnt:
        ans = 0
        break

print(ans)