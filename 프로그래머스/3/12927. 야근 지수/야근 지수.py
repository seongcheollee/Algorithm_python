# 야근 피로도 = 야근 시작시점 + 남은 일의 작업량**2
import heapq

def solution(n, works):
    
    if n > sum(works):
        return 0
    
    works = [-x for x in works]

    heapq.heapify(works)
    
    for i in range(n):
        k =  heapq.heappop(works)
        k += 1
        heapq.heappush(works, k)

    return sum(x**2 for x in works)