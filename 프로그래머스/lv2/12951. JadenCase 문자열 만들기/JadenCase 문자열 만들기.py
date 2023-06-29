def solution(s):
    res = []
    sList = s.split(' ')
    for i in sList:
        res.append(i.capitalize())

    # join 사용시 공백까지 같이 추가
    return " ".join(res)
