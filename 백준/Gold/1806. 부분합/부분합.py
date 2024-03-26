n , s = map(int, input().split())
nums = [0] + list(map(int, input().split()))

for i in range(1,n+1):
    nums[i] += nums[i-1]
l = 0
r = 0
res = n+1
while l <= r and r < n+1:

    t = nums[r] - nums[l]
    if t < s:
        r += 1
    else:
        res = min(res , r-l)
        l += 1

if res == n+1:
    print(0)
else:
    print(res)
