import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

stk = []
res = []
i = 1

while nums:
    if not stk:
        stk.append(i)
        res.append('+')
        i += 1
        continue

    if stk[-1] < nums[0]:
        stk.append(i)
        res.append('+')
        i += 1
    elif stk[-1] == nums[0]:
        stk.pop()
        nums.pop(0)
        res.append('-')
    else:
        print('NO')
        break

if not nums:
    for i in res:
        print(i)