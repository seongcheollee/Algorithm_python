from collections import deque

n = int(input())
q = deque([i for i in range(1,n+1)])

for i in range(n):
    if len(q) > 1:
        q.popleft()
        q.append(q.popleft())
        
print(q[0])
