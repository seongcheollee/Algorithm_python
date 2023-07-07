def solution(k, tangerine):
    dic = {}
    n = 0
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for i in sorted_dict:
        if k > 0:
            k -= sorted_dict[i]
            n += 1
            
    return n
