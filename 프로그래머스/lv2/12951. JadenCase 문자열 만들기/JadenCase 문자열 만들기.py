def solution(s):
    res = []
    sList = s.split(' ')
    for i in sList:
        res.append(i.capitalize())

    return " ".join(res)
