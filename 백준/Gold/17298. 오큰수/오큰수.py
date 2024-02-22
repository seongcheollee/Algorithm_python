n = int(input())

nums = list(map(int, input().split(' ')))
res = [-1] * n

stk = []

for i in range(n):
    while stk and stk[-1][0] < nums[i]:
        num , idx = stk.pop()
        res[idx] = nums[i]

    stk.append((nums[i],i))

for i in res:
    print(i, end=' ')