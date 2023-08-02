import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


n = int(input())
l = int(input())

network = [[] for i in range(n+1)]
visited = [False] * (n+1)


for i in range(l):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

cnt = 0

def dfs(start):
    global cnt
    visited[start] = True

    for i in network[start]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)
dfs(1)
print(cnt)