from itertools import combinations
from collections import defaultdict
def solution(word):
    words = 'AEIOU'
    dic = defaultdict(int)
    global k
    k = 1
    
    def dfs(cnt, w):
        global k
        if cnt == 5:
            return
        for i in range(len(words)):
            dic[w+words[i]] += k
            k += 1
            dfs(cnt+1, w+words[i])
            
    dfs(0,"")
    
    return dic[word]
