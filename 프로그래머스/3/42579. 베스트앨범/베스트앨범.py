from collections import defaultdict

def solution(genres, plays):
    res = []
    dic = defaultdict(list)
    dic_cnt = defaultdict(int)

    for i in range(len(genres)):
        dic[genres[i]].append((plays[i],i))
        dic_cnt[genres[i]] += plays[i]
    
    for k in dic:
        dic[k].sort(key=lambda x : x[1])
        dic[k].sort(reverse=True,key=lambda x : x[0])

        
    dic_cnt = dict(sorted(dic_cnt.items(), key=lambda x : x[1], reverse=True))
    
    
    for d in dic_cnt:
        if len(dic[d]) == 1:
            res.append(dic[d][0][1])
        else:
            for i in range(2):
                res.append(dic[d][i][1])
                
    
    return res

a = ["classic", "pop", "classic", "classic", "pop"]
b = [100, 100, 100, 100, 100]
solution(a,b)