from collections import deque
T = int(input())

for i in range(T):
    n, m = map(int, input().split(' '))
    q = deque(list(map(int, input().split(' '))))
    cnt = 0

    # 큐
    while q:
        # 현재 출력할 것
        pn = q.popleft()

        if not q:
            print(cnt+1)
            break
        else:
            qm = max(q)

        if pn < qm:
            q.append(pn)
            m = (m - 1 + len(q)) % len(q)
        else:
            if m == 0:
                print(cnt+1)
                break
            cnt += 1
            m = (m - 1 + len(q)) % len(q)



