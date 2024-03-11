from collections import deque
def solution(x, y, n):
    answer = 0
    cnt = [0] * (y+1)
    
    q = deque([x])
    
    if x == y:
        return 0
    
    
    while q:
        nx = q.popleft()
        
        for i in (nx+n, nx*2, nx*3):
            
            if i > y or cnt[i]:
                continue
                
            if i == y:
                return cnt[nx] + 1
            
            cnt[i] = cnt[nx] + 1
            q.append(i)
                

    
    
    return -1