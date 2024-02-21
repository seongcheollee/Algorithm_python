import sys
input = sys.stdin.readline

n = int(input())
buildings = []
for i in range(n):
    buildings.append(int(input()))

res = [0] * n
stk = []
for i in range(n):
    if not stk:
        stk.append((buildings[i], i))
        continue

    while stk and stk[-1][0] <= buildings[i]:
        h, w = stk.pop()
        res[w]= i - w - 1


    stk.append((buildings[i], i))


while stk:
    h, w = stk.pop()
    res[w] = n - w - 1

print(sum(res))