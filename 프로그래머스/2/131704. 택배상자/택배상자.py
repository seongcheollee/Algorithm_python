from collections import deque
def solution(order):

    q = deque(order)
    temp_container = [] 
    
    cnt = 0
    for i in range(1, len(order)+1):
        temp_container.append(i)
        
        while temp_container and temp_container[-1] == q[0]:
            temp_container.pop()
            q.popleft()
            cnt += 1
            
    
    return cnt

# order -> 큐
# temp_container -> 스택

