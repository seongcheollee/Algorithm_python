from collections import deque

q = deque()
buffer =  int(input(''))
while True:

    n = int(input(''))

    if n == 0:
        q.popleft()
    elif n == -1:
        break
    else:
        if len(q) < buffer:
            q.append(n)


if q:
    for i in q:
        print(i ,end=' ')
else:
    print('empty')



