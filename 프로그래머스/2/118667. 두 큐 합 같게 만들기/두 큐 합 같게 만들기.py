from collections import deque

def solution(queue1, queue2):
    cnt = 0
       
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 =sum(q1)
    s2 =sum(q2)
    limit = len(q1) * 4
    s = s1 + s2
    
    if s % 2 != 0:
        return -1
    
    while True:
        if s1 < s2:
            temp = q2.popleft()
            q1.append(temp)
            s1 += temp
            s2 -= temp
            cnt += 1
        elif s1 > s2:
            temp = q1.popleft()
            q2.append(temp)
            s1 -= temp
            s2 += temp
            cnt += 1
        else:
            break
            
        if cnt == limit:
            return -1
            
    return cnt 