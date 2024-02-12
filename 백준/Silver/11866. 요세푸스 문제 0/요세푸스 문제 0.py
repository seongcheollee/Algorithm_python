import sys

input = sys.stdin.readline
n, k = map(int, input().split(' '))

nums = [i for i in range(1,n+1)]
i = k - 1
res = []

if len(nums) == 1:
    res = nums
else:
    while nums:
        res.append(nums.pop(i))
        n -= 1
        i = (i + k - 1) % n

        if n == 1:
            res.append(nums.pop())

print("<",end="")
for i in range(len(res)-1):
    print(res[i],end=", ")
print(res[-1], end = "")
print(">",end="")