import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
nums = []
for i in range(n):
    nums.append(int(input()))

nums.sort()

res = float("inf")
left = 0
right = 0

while left <= right and right < n:
    k = nums[right] - nums[left]

    if k < m:
        right += 1
    elif k > m:
        res = min(res, k)
        left += 1
    else:
        res = m
        break
print(res)