# 문제 요약 : 특정 인덱스로부터 오름차 순의 길이 카운트
from collections import deque
def solution(prices):
    res = []
    q = deque(prices)
    
    while q:
        k = q.popleft()
        cnt = 0
        
        for i in q:
            cnt += 1
            if k > i:
                break
    
        res.append(cnt)
            
    
    return res

print(solution([1,1,1,1]))