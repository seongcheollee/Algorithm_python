def solution(n):
    
    def ntob(n):
        b = ''
        while n > 1:
            b += str(n % 2)
            n //= 2
        b += str(n)
        
        return b.count('1')
        
    point = ntob(n)
    
    while True:
        n += 1
        if ntob(n) == point:
            return n
        
    return n