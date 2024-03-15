import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(1,n):
    nums[i] += nums[i-1]

res = [nums[k-1]]
for i in range(k,n):
    res.append(nums[i] - nums[i-k])


print(max(res))
