# 문제 요약 : 연결된 네트워크 개수 찾기
# 문제 풀이
# 1. 전형적인 dfs 문제로 노드들을 방문 하면서 방문배열 연결여부 체크
# 2. 연결여부 체크 후 해당 노드들을 한 개의 네트워크로 반환
# 3. 각각의 노드들을 돌 때 이미 다른 것과 연결되어 있을시 return 0 하여 없는 것으로 간주

def solution(n, computers):
    cnt = 0
    v = [0] * n  # 방문 확인 배열
    
    def dfs(i):
        # 방문 여부 체크
        if v[i]:
            return 0
        # 방문 표시
        v[i] = 1

        # 반복문 돌면서 갈 수 있는 노드 진입 
        for j in range(n):
            # 방문할 수 있고, 방문되지 않았던 노드이면
            if computers[i][j] and not v[j]:
                # 방문
                dfs(j)

        # 방문 체크 완료후 리턴
        return 1

    # 배열의 노드들 돌면서 dfs 실행
    for i in range(n):
        if dfs(i):
            cnt += 1

    return cnt
