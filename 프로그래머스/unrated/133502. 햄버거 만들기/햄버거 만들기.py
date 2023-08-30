from collections import deque

def solution(ingredient):
    cnt = 0
    ham = [1,2,3,1]

    stk = []
    q = deque(ingredient)
    
    while q:
        stk.append(q.popleft())

        if stk[-4:] == ham:

            for i in range(4):
                stk.pop()
            cnt += 1
    
        
    return cnt


