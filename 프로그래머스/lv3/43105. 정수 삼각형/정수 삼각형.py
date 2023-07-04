def solution(triangle):
    # 삼각형 내려가기
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 양 사이드 끝에 대한 조건 걸기
            # 사이드 끝은 한 가지 밖에 더할 수 없음
            if j == 0:
                # 왼쪽 끝은 윗층의 j= 0일때
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                # 오른쪽 끝은 현재 길이에서 -1한 인덱스의 위치 값 더하기
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 나머지는 윗층 인덱스에서 자신과 같은 인덱스와, 자신보다 1 작은 인덱스 중 큰 값
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    
    return max(triangle[-1])