import heapq
from collections import deque

def solution(jobs):
    heap =[]
    tot = 0
    now = 0
    start = -1
    i = 0
    
    while i < len(jobs):
        
        # 현재 처리가능한 잡들 삽입
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap,  [j[1], j[0]])
        
        
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            tot += (now - curr[1])
            i += 1
        else:
            now += 1

    
    return tot // len(jobs)
    
  

