def solution2(s, n):
    res = ''
    for i in s:
        if i.isalpha():
            res += next_alpha(i,n)
        else:
            res += ' '

    return res

def next_alpha(s,n):
    if s.islower():
        return chr(((ord(s)-ord('a')+n)%26) + ord('a'))
    elif s.isupper():
        return chr(((ord(s)-ord('A')+n)%26) + ord('A'))

def solution(s, n):
    answer = []
    for i in s: 
        if i == ' ' :
            answer.append(' ') 
        else :                 
            if i.islower(): 
                answer.append(chr((ord(i) - ord('a') + n) % 26 + ord('a')))

            elif i.isupper() : 
                answer.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
            
    return ''.join(answer)