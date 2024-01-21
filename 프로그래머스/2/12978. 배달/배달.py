import heapq

def solution(N, road, K):
    res = 0
    INF = int(1e9)
    # N 마을 개수
    # K 거리 이하만 배달 가능
    # 배달가능한 마을 카운트 (시작 노드는 1)
    dist = [INF] * (N+1)
    g = [[] for i in range(N+1)]
    for r in road:
        a,b,c = r
        g[a].append((b,c))
        g[b].append((a,c))
        
    def dijkstra(s):
        q = []
        heapq.heappush(q, (0,s))
        dist[s] = 0
        
        while q:
            d, c = heapq.heappop(q)
            if dist[c] < d:
                continue
            
            for i in g[c]:
                temp = d + i[1]
                
                if temp < dist[i[0]]:
                    dist[i[0]] = temp
                    heapq.heappush(q, (temp, i[0]))
            print(q)
            print(dist[1:])
    
    dijkstra(1)
    for i in dist:
        if i <= K:
            res += 1
    
    return res