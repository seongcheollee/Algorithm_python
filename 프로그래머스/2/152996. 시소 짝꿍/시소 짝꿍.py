from collections import Counter

def solution(weights):
    cnt = 0  
    w_dic = {}
    
    for w in weights:
        if w not in w_dic:
            w_dic[w] = 0
        w_dic[w] += 1
        
    weights = set(weights)
    
    # n개의 같은 수의 조합 경우의 수 = n * (n-1) // 2
    for i in weights:
        if w_dic[i] > 1:
            cnt += (w_dic[i] * (w_dic[i]-1)) // 2
    # print(w_dic)
    # print(cnt)

    for w in weights:
        if w*3/2 in weights:
            cnt+= w_dic[w*3/2] * w_dic[w]
        if w*2 in weights:
            cnt+= w_dic[w*2] * w_dic[w]
        if w*4/3 in weights:
            cnt+= w_dic[w*4/3] * w_dic[w]

    return cnt


# 2 2 = 같을때
# 2 3 =  3/2 가 있을떄
# 2 4 =  2배가 있을때
# 3 4 =  4/3 이 있을때