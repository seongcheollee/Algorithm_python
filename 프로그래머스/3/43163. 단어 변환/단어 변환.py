from collections import deque

def solution(begin, target, words):
    res = 0
    INF = int(1e9)
    visited = [INF] * (len(words) +1)
    if not target in words:
        return 0
    
    
    def check_change_word(s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        return cnt == 1 
    # 모든 경우의 수 중에서 가장 짧은 애
    # 
    def bfs():
        q = deque([(begin, 0)])

        while q:
            
            s, c = q.popleft()
            
            if s == target:
                return c
                            
            for w in words:
                if check_change_word(s,w):
                    q.append((w, c+1))
        
        
    return bfs()
