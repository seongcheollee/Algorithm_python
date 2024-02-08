def solution(topping):
    
    # 딕셔너리 구조를 사용한 탐색. 
    # 처음에는 시간초과로 너무 어렵게 이분탐색을 고려 했으나, 딕셔너리 탐색도 고려 할 것.
    cheolSu = {}
    brother = {}
    cnt = 0
    
    for t in topping:
        if t in cheolSu:
            cheolSu[t] += 1
        else:
            cheolSu[t] = 1    
            
    for t in topping:
        
        if len(brother) == len(cheolSu):
            cnt += 1
            
        if t in brother:
            brother[t] += 1
        else:
            brother[t] = 1
        
        cheolSu[t] -= 1    
            
        if cheolSu[t] == 0:
            del cheolSu[t] 
            
    return cnt