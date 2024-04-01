import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for i in range(n+1)]

INF = int(1e9)
dist = [1e9] * (n+1)

for i in range(m):
    s, e, v = map(int, input().split())
    g[s].append((e,v))
start, end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    dist[start] = 0

    while q:
        d, node = heapq.heappop(q)

        if dist[node] < d:
            continue

        for next, nd in g[node]:
            cost = d + nd
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(q, (cost, next))


dijkstra(start)
print(dist[end])
