from collections import deque

def solution(priorities, location):
    res = 0
    q = deque(priorities)
    l = len(priorities) - 1 # 최초 큐의 길이 
    while q:
        # 가장 앞에 존재하는 job pop
        n = q.popleft()        
        
        # 우선 순위 찾는 프로세스
        
        # 큐에 비교할 다른 job이 존재할 때
        if q:
            # 우선순위 판별
            if n < max(q):
                # 실패시 큐의 맨 뒤로 작업 변경
                q.append(n)
                # 찾고자하는 위치 값 변경
                location -= 1
                if location == -1:
                    location = l
            else:
                # job 완료 -> 큐 길이 변경
                l -= 1
                # 찾고자하는 위치 값 변경
                location -= 1
                res += 1
                # 작업 완료한 job이 location인 경우
                if location == -1:
                    return res
                
        # 큐가 비어있는 경우 (우선순위가 가장 낮아 큐에 아무것도 존재하지 않을 때) 
        else: 
            res += 1
    
    return res