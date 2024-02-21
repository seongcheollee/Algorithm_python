import sys
input = sys.stdin.readline

n = int(input())


g = []
for i in range(n):
    g.append(input())

global res
res = ''
def dfs(x,y,n):
    global res

    if n == 1:
        res += '{}'.format(g[x][y])
        return

    stand = g[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if g[i][j] != stand:
                res += '('
                n //= 2
                # 1사
                dfs(x,y,n)
                # 2
                dfs(x, y+n, n)
                # 3
                dfs(x+n, y, n)
                # 4
                dfs(x+n, y+n, n)
                res += ')'
                return

    res+= str(stand)
    return

dfs(0,0,n)
print(res)