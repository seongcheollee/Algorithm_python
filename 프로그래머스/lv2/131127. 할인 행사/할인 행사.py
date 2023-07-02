def solution(want, number, discount):
    cnt = 0
    dic = {}
    dis_len = len(discount) # discount 길이
    l = sum(number) # 사야 할 상품의 총 개수
    
    # want number -> dict()
    # dic.update(zip(want, number)) 딕셔너리 정의 함수
    for i in range(len(want)):
        dic[want[i]] = number[i]

    # 필요(최소) 반복 횟수 discount의 길이
    # discount의 길이를 1씩 줄여나가면서 want의 품목이 모두 있는지 확인.
    for i in range(dis_len):
        
        # 탐색 길이가 요구 길이 보다 작을 시 값 리턴
        if i + l > dis_len:
            return cnt
        
        n_dis = discount[i:i+l]
        # 구매한 항목 변수 초기화
        parchase = 0
        for p in dic:
            if n_dis.count(p) == dic[p]:
                parchase += 1
        
        # 모든 항목 구매시 cnt + 1
        if parchase == len(dic):
            cnt += 1
        
    return cnt