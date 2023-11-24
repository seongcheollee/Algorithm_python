def solution(today, terms, privacies):
    answer = []
    terms_hash = {}
    for t in terms:
        terms_hash[t.split(' ')[0]] = int(t.split(' ')[1]) * 28

    ny, nm, nd = map(int, today.split('.'))
    i = 1
    for p in privacies:
        p, t =  p.split(' ')
        py, pm, pd = map(int, p.split('.'))
        
        if ((ny - py) * 12* 28) + (nm - pm)*28 + nd - pd >= terms_hash[t]:
            answer.append(i)
        i += 1
    
    return answer