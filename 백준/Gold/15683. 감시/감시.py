import copy

n , m = map(int, input().split())

g = [list(map(int, input().split())) for i in range(n)]
cctv = []
min_v = int(1e9)

for i in range(n):
    for j in range(m):
        if 1 <= g[i][j] <= 5:
            cctv.append((g[i][j],i,j))

direct = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def fill(g, direction, x,y):
    for i in direction:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if g[nx][ny] == 6:
                break
            elif g[nx][ny] == 0:
                g[nx][ny] = -1

def dfs(d, g):
    global min_v
    if d == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += g[i].count(0)
        min_v = min(min_v, cnt)
        return

    temp = copy.deepcopy(g)
    cctv_n ,x,y = cctv[d]

    for i in direct[cctv_n]:
        fill(temp, i, x, y)
        dfs(d+1, temp)
        temp = copy.deepcopy(g)

dfs(0, g)
print(min_v)