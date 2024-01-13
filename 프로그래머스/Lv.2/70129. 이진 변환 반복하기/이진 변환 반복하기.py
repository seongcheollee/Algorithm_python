def solution(s):
    answer = []
    cnt = 0
    removed_zero = 0
    
    def ntob(n):
        b = ''
        while n > 1:
            b += str(n % 2)
            print(b)
            n = n // 2
        b += str(n)
        return b[::-1]
        
    while s != '1':
        n = s.count('1')
        removed_zero += len(s) - n
        s = ntob(n)    
        cnt += 1
    
    return [cnt, removed_zero]

    