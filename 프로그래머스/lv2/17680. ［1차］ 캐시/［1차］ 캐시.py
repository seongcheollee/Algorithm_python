def solution(cacheSize, cities):
    arr = []
    cnt = 0
    
    # 도시 이름 하나 가져오기
    for ct in cities:
        # 대소문자 구분없애기
        ct = ct.lower()
        
        if ct in arr:
            arr.remove(ct)
            arr.append(ct)
            cnt += 1
        else:
            arr.append(ct)
            cnt += 5
        
        if len(arr) > cacheSize:
            arr.pop(0)
            
    
    return cnt