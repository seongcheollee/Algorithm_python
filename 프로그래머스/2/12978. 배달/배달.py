import heapq
from math import inf
def solution(N, road, K):

    # 그래프 변형 g[방문지점] = [연결된 노드, 거리]
    g = [[] for _ in range(N+1)]
    for i,j,w in road:
        g[i].append([j,w])
        g[j].append([i,w])
    
    queue = [] # heapq 에 넣을 배열 생성
    visited = [inf] * (N+1) # 방문시 최단 거리를 추가해주기 위한 배열
    
    heapq.heappush(queue,[1, 0])  #시작점 삽입, [노드, 거리]
    visited[1] = 0 # 시작 지점 거리 값 초기화
    
    while queue:
        # 다음 방문할 노드와 거리 추출   
        node, dist = heapq.heappop(queue)
        
        # 다음 방문 노드
        for n, d in g[node]:
            # 현재 거리와 추가될 거리 비교
            if dist + d < visited[n]:
                visited[n] = dist + d
                # 다음 탐색을 위한 힙 푸시
                heapq.heappush(queue, [n, dist + d])
    print(visited)
    return len([i for i in visited if i <=K])