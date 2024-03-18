from collections import deque

word = input()
q = deque(list(word))
boom = input()
n = len(boom)

stk = []

for w in word:
    stk.append(w)
    if len(stk) >= n and ''.join(stk[-n:]) == boom:
        for _ in range(n):
            stk.pop()

if stk:
    print(''.join(stk))
else:
    print('FRULA')
