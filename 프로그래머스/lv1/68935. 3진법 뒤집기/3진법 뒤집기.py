def solution(n):
    res = 0
    
    # n -> 3진법
    def nto3(n):
        st = ''
        # 종료 조건
        while n > 2:
            # 나머지 더하고 값변환
            st += str(n % 3)
            n //= 3
        # 마지막 몫 삽입
        st += str(n)
        # 리버스해서 변환
        return st[::-1]
    
    n = nto3(n)
    # 지수가 0일 때
    k = 1
    
    for i in n:
        res += k * int(i)
        k *= 3
    
    
    return res
