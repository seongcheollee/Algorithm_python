# 문제 요약 : 특정 인덱스로부터 오름차 순의 길이 카운트
from collections import deque

def solution(prices):
    res = []
    q = deque(prices)
    
    while q:
        # 큐에서 비교할 기준 값 뽑기
        k = q.popleft()
        cnt = 0
        # 기준값이 사라진 큐 반복문 돌면서 가격이 떨어지는지 확인
        for i in q:
            cnt += 1
            if k > i:
                break
        
        res.append(cnt)
                
    return res

"""
        처음 구성
        for i in q:
            
            if k <= i:
                cnt += 1
        
        해당 구성의 문제점
        1. prices 리스트 전체를 순회함.
        -> 이미 하락이 되었음에도 cnt 값을 체크하는 문제 발생
"""
