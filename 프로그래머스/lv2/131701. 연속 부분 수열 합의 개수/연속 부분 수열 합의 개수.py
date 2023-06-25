def solution(elements):
    # 중복 제거를 위한 set 선언
    res = set()
    # 범위 초과 방지를 위해 길이를 늘려줌.
    elements *= 2
    
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
             res.add(sum(elements[i:i+j+1]))
    
    return len(res)

# 