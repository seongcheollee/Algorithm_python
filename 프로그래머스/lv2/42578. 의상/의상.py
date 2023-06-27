def solution(clothes):
    dic = {}
        
    # 각 카테고리 별 개수 파악
    for item in clothes:
        name, category = item
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
    
    # n개의 개수를 가진 하나의 카테고리에서 나올 수 있는 가지 수  = n + 1
    # + 1 은 아무것도 입지 않은 경우
    s = 1
    # 모든 경우의 수 구하기
    for i in dic:
        s *= (dic[i]+1)
        
        
    return s - 1