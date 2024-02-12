def isVps(s):
    stk = []

    for i in s:
        if not stk:
            stk.append(i)
        else:
            if i == '(':
                stk.append(i)
            else:
                if stk[-1] != '(':
                    return 'NO'
                else:
                    stk.pop()

    if stk:
        return 'NO'
    else:
        return 'YES'



T = int(input())

for i in range(T):
    print(isVps(input('')))


