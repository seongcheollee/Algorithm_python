from collections import deque

# 블록제거

def bfs(x,y):
    res = []
    q = deque([(x,y)])
    v = [[0] * 6 for i in range(12)]
    v[x][y] = 1
    while q:
        x, y = q.popleft()
        res.append([x,y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<= nx < 12) and (0 <= ny < 6) and (v[nx][ny] == 0):
                if g[nx][ny] == g[x][y]:
                    q.append((nx,ny))
                    v[nx][ny] = 1

    if len(res) < 4:
        return 0
    else:
        for r in res:
            g[r[0]][r[1]] = '.'
        return 1

def update(x,y):

    while 0 <= x < 11:

        x += 1
        if g[x][y] == '.':
            g[x][y] = g[x-1][y]
            g[x - 1][y] = '.'
        else:
            break

g = []

for i in range(12):
    g.append(list(input()))
dx = [0,1,-1,0]
dy = [1,0,0,-1]

ans = 0

while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if g[i][j] in ('R','G','B','P','Y'):
                cnt += bfs(i,j)

    if not cnt:
        break
    else:
        ans += 1

    for i in range(10,-1,-1):
        for j in range(5,-1,-1):
            if g[i][j] in ('R','G','B','P','Y'):
                update(i,j)
                
    # for i in g:
    #     print(i)# 업데이트 그래프
    # 
    # print()

print(ans)