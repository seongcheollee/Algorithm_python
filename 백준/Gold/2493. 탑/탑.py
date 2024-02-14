import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split(' ')))
res = [0 for _ in range(n)]
stk = []

for i in range(n):
    if not stk:
        stk.append(nums[i])
        continue

    if stk[-1] >= nums[i]:
        res[i] = i
    else:
        j = i
        while j > 0:
            if nums[res[j-1]-1] >= nums[i]:
                res[i] = res[j-1]
                break
            else:
                j -= 1

    stk.append(nums[i])



print(' '.join(map(str, res)))

