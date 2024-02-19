from collections import deque

r, c = map(int, input().split(' '))
g = []
jv = [[0 for _ in range(c)] for i in range(r)]
fv = [[0 for _ in range(c)] for i in range(r)]

jq = deque()
fq = deque()

for i in range(r):
    g.append(input(''))

for i, x in enumerate(g):
    for j, y in enumerate(x):
        if g[i][j] == 'J':
            jq.append((i,j))
            jv[i][j] = 1
        if g[i][j] == 'F':
            fq.append((i, j))
            fv[i][j] = 1

def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while fq:
        x,y = fq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if g[nx][ny] != '#' and fv[nx][ny] == 0:
                    fv[nx][ny] = fv[x][y] + 1
                    fq.append((nx,ny))
    while jq:
        x,y = jq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에서
            if 0 <= nx < r and 0 <= ny < c:
                # 벽이 아니고, 지나갔던 길이 아니면
                if g[nx][ny] != '#' and jv[nx][ny] == 0:
                    # 불이 번져있지 않거나, ㅂ
                    if fv[nx][ny] == 0 or jv[x][y] + 1 < fv[nx][ny]:
                        jv[nx][ny] = jv[x][y] + 1
                        jq.append((nx,ny))
            else:
                return jv[x][y]

    return "IMPOSSIBLE"
print(bfs())
