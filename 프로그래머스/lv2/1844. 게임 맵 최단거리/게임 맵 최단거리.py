from collections import deque

def solution(maps):
    # 가로 세로 길이
    n = len(maps)
    m = len(maps[0])
    
    def bfs(x,y,n,m):
        
        # 시작 인덱스 고정
        q = deque()
        q.append((x,y))
        
        # 가로세로 이동
        dx = [1, -1, 0, 0] 
        dy = [0, 0, 1, -1]

        # bfs
        while q:
            x,y = q.popleft()
        
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]
                
                # 이동 범위 제한
                if (0 <= nx < n) and (0 <= ny < m):
                    if maps[nx][ny] == 1:
                        q.append((nx, ny))
                        maps[nx][ny] += maps[x][y]
            
        return maps[n-1][m-1]
    res = bfs(0,0,n,m)
    if res == 1:
        return -1
    else:
        return res