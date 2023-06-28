from collections import deque

def solution(priorities, location):
    res = 0
    q = deque(priorities)
    l = len(priorities) - 1
    while q:
        print(q)
        # 가장 앞에 존재하는 job pop
        n = q.popleft()        
        # 우선 순위 찾는 프로세스
        
        if q:
            if n < max(q):
                q.append(n)
                location -= 1
                if location == -1:
                    location = l
            else:
                l -= 1
                location -= 1
                res += 1
                if location == -1:
                    return res
        else:
            res += 1
    
    return res

print('답',solution([1,2,3,4,5,6,7],0))