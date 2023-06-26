def solution(cacheSize, cities):
    
    cache = []
    cnt = 0
    
    # 도시 이름 하나 가져오기
    for ct in cities:
        # 대소문자 구분없애기
        ct = ct.lower()
        
        if ct in cache:
            # 중복된 값이 존재할 시 LRU 에 따라서 현재 값 가장 뒤로 이동 
            cache.remove(ct)
            cache.append(ct)
            # 캐시 hit
            cnt += 1
        else:
            # 중복된 값이 없음
            cache.append(ct)
            # 캐시 miss
            cnt += 5
            if len(cache) > cacheSize:
                cache.pop(0)
        
        
        # 캐시 사이즈 넘으면 가장 사용되지 않은 값 pop
                    
    
    return cnt