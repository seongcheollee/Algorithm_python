from collections import defaultdict
def solution(tickets):
    
    res = []
    dic = defaultdict(list)
    tickets.sort(key=lambda x:x[1])
    
    for a,b in tickets:
        dic[a].append(b)
    
    def dfs(s):
        while dic[s]:
            dfs(dic[s].pop(0))
        res.append(s)
        
    dfs('ICN')
    
    return res[::-1]