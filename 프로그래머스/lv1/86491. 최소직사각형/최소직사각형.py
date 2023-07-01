def solution(sizes):
    # max width, max height 
    mw = 0
    mh = 0
    # 정렬
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
    # mw 는 큰 수들 중 가장 큰 것
    # mh는 작은 수들 중 가장 큰 것
    for size in sizes:
        if mw < size[0]:
            mw = size[0]
        if mh < size[1]:
            mh = size[1]
    
    return mw * mh