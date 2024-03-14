n , m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

move = [list(map(int, input().split())) for _ in range(m)]

curr = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dy = [0,0,-1,-1, -1,0,1,1,1]
dx = [0,-1,-1 ,0, 1,1, 1,0,-1]


dx2 = [1,1,-1,-1]
dy2 = [1,-1,1,-1]

def move_cloud(d, c):
    for i in range(len(curr)):
        curr[i][0] = (curr[i][0] + dy[d] * c + n) % n
        curr[i][1] = (curr[i][1] + dx[d] * c + n) % n

        g[curr[i][0]][curr[i][1]] += 1

def inc_water():
    for r,c in curr:
        cnt = 0
        for i in range(4):
            nx = r + dx2[i]
            ny = c + dy2[i]

            if 0<= nx < n and 0 <= ny < n and g[nx][ny]:
                cnt += 1

        visited[r][c] = 1
        g[r][c] += cnt


def remove_water():
    cloud = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and g[i][j] > 1:
                g[i][j] -= 2
                cloud.append([i,j])
    return cloud


for i, c in move:
    move_cloud(i, c)
    visited = [[0]*n for _ in range(n)]
    inc_water()
    curr = remove_water()

    # for i in g:
    #     print(i)
    # print()



k = 0
for i in g:
    k += sum(i)
print(k)