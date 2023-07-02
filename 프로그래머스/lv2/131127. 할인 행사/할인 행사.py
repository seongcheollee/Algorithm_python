def solution(want, number, discount):
    cnt = 0
    dic = {}
    dis_len = len(discount)
    l = sum(number)
    
    for i in range(len(want)):
        dic[want[i]] = number[i]
    # dic.update(zip(want, number)) 딕셔너리 정의 함수 사용
    
    # 필요(최소) 반복 횟수 discount의 길이
    # discount의 길이를 1씩 줄여나가면서 want의 품목이 모두 있는지 확인.
    for i in range(dis_len):
        
        if i + l > dis_len:
            return cnt
        
        n = discount[i:i+l]
        t = 0
        for p in dic:
            if n.count(p) == dic[p]:
                t += 1
                
        if t == len(dic):
            cnt += 1
        
    
    
    return cnt