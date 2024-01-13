def solution(n):
    # 연속한 자연수의 합으로 n을 만드는 방법
    # 브투트 포스? 수학 공식?
    
    res = 0
    for i in range(1, n+1):
        s = 0
        for j in range(i,n+1):
            s += j
            if s >= n:
                break
        if s == n:
            res += 1

            
    
    
    return res