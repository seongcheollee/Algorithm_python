import sys

input = sys.stdin.readline
n, k = map(int, input().split(' '))

nums = [i for i in range(1,n+1)]
i = 0
res = []

while nums:
    i = (i + k - 1) % n
    res.append(nums.pop(i))
    n -= 1

print("<",end="")
for i in range(len(res)-1):
    print(res[i],end=", ")
print(res[-1], end = "")
print(">",end="")