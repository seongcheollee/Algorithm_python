def solution(n):
    res = 0
    
    def nto3(n):
        st = ''
        while n > 2:
            st += str(n % 3)
            n //= 3
        st += str(n)
        return st[::-1]
    
    n = nto3(n)
    k = 1
    
    for i in n:
        res += k * int(i)
        k *= 3
    
    
    return res
