import sys

def check_stk(s):
    stk = []
    for i in s:
        if not stk:
            stk.append(i)
        else:
            if i == ')':
                if stk[-1] == '(':
                    stk.pop()
                else:
                    return 'no'
            elif i == ']':
                if stk[-1] == '[':
                    stk.pop()
                else:
                    return 'no'
            else:
                stk.append(i)
    if stk:
        return 'no'
    else:
        return 'yes'


a = ['(',')','[',']']

while True:
    s = input("")
    if s == ".":
        break

    filter_s = ''

    for i in s:
        if i in a:
            filter_s += i

    print(check_stk(filter_s))