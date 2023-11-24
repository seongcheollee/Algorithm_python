def solution(today, terms, privacies):
    res = []
    terms_hash = {}
    
    # 계약기간 해시테이블 월 -> 일 기준으로
    for t in terms:
        terms_hash[t.split(' ')[0]] = int(t.split(' ')[1]) * 28
    
    # 현재 년,월,일
    ny, nm, nd = map(int, today.split('.'))
    
    for i, p in enumerate(privacies):
        # 수집 일자,약관 종류
        p, t =  p.split(' ')
        # 수집 일자 년 월 일
        py, pm, pd = map(int, p.split('.'))
        
        # 총 지난 일자 계산
        if ((ny - py) * 12* 28) + (nm - pm)*28 + nd - pd >= terms_hash[t]:
            res.append(i+1)
    
    return res