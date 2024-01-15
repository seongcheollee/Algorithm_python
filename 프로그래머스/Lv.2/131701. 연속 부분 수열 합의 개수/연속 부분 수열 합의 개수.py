def solution(elements):
    answer = 0
    res = set()
    n = len(elements)

    elements_2 =  elements * 2
    
    for i in range(1,n+1):
        s = 0
        for j in range(n):
            res.add(sum(elements_2[j:j+i]))
            
            
            
            
    
    
    return len(res)