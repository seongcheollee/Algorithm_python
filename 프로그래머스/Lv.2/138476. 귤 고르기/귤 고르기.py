# k 개를 이룰 수 있는 귤의 가지수 최소개

def solution(k, tangerine):
    answer = 0
    
    n = len(tangerine) # 상자 안에 담긴 귤의 개수 8 7
    t = 0
    dic = {}
    
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    cnt_list = list(dic.values())
    cnt_list.sort(reverse=True)
    
    s = 0
    for i in cnt_list:
        s += i
        t += 1
        
        if s >= k:
            return t
        
        
    return t