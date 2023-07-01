def solution(s):
    res = []
    # s에서 숫자만
    s = s.replace('{', '')
    s = s.split('},')
    for i in range(len(s)):
        s[i] = s[i].replace('}','')
    s = sorted(s, key=len)

    for i in s:
        i = i.split(',')
        for j in i:
            if not int(j) in res:
                res.append(int(j))

    return res