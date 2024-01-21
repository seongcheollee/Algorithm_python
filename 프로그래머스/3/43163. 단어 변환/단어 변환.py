from collections import deque

def solution(begin, target, words):
    
    
    # 변환 불가 0 리턴
    if not target in words:
        return 0
    
    # 변환 가능 여부 체크
    def check_change_word(s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        return cnt == 1 

    # 최단 거리이기 때문에 target에 가장 빨리 도착하는 카운트를 세면 됨.
    def bfs():
        
        # 단어와 카운트 변수 큐에 삽입 
        q = deque([(begin, 0)])

        while q:
            
            s, c = q.popleft()
            
            # 타겟 방문시 카운트 리턴
            if s == target:
                return c
            
            # 단어목록을 방문하면서 조건 충족시 큐에 추가
            for w in words:
                if check_change_word(s,w):
                    # 카운트 변수의 경우 +1 
                    q.append((w, c+1))
        
        
    return bfs()
