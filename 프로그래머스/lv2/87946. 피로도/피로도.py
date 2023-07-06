# 문제 요약 : 피로도를 효율적으로 활용하여 최대한 많은 던전을 돌자.
# 문제 풀이 방식:
# 1. 주어진 피로도 k를 가지고, 던전에서 요구하는 최소필요도, 소모필요도 파악
# 2. 최소 필요도를 만족하면 해당 던전을 돌고, 피로도 k 차감
# 3. 남은 방식으로 나머지 던전 진입가능 여부 확인
# 4. 총 완료한 던전의 개수 세기
# 5. 던전마다 피로도 소모가 다르기 때문에 가장 최적의 효율을 찾아야함.
# 6. 모든 던전의 경우의 수를 탐색하여 진입횟수가 가장 높은 경우의 진입횟수를 반환

def solution(k, dungeons):
    global cnt
    cnt = 0
    v = [0] * len(dungeons)
    
    
    def dfs(n,p,t): # n : 현재 노드의 인덱스 , p : 피로도, t: 카운트하기 위한 변수
        # 방문 여부 확인
        global cnt
        if cnt < t:
            cnt = t
        
        for i in range(len(dungeons)):
            # 방문하지 않고, 입장가능한 던전
            if not v[i] and dungeons[i][0] <= p:
                v[i] = 1
                dfs(i, p - dungeons[i][1],t+1)
                # 모든 경우의 수를 탐색하기 위해서 백트래킹
                v[i] = 0
    
    dfs(0,k,0)
    
    return cnt
    