def solution(n):
    res = ''
    # 0 1 2 인덱스
    k = [1,2,4]
    
    # 3진법 코드
    while n > 0:
        n -= 1
        t = str(k[n % 3])
        n = n // 3
        res += t
        
    if n != 0:
        res += str(n)

    res = res[::-1]
    
    return res

