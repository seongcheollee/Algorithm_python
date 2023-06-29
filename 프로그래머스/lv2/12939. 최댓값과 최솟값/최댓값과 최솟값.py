def solution(s):
    a = list(map(int, s.split(' ')))
    
    return '{} {}'.format(min(a), max(a))