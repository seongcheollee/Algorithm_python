def solution(b, y):
    res = []
    for i in range(1,((b+y)//2)+1):
        if (b+y) % i == 0:
            if i >= 3 and (b+y)//i >= 3:
                if i >= (b+y) // i:
                    res.append([i,(b+y)//i])

    for sq in res:
        if sq[0] * 2 + (sq[1] - 2) * 2 == b:
            return [sq[0], sq[1]]
        
        
    
    
    return res