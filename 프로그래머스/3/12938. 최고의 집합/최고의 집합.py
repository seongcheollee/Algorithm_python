def solution(n, s):
    res = [s//n] * n
    
    if s < n:
        return [-1]
    
    for i in range(s-sum(res)):
        res[i%n] += 1
        
    res.sort()
    return res

