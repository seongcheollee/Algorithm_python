import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
for i in range(n):
    a, l, r = input().split()
    nums = [0] * len(s)

    for j in range(len(s)):
        if s[j] == a:
            nums[j] += 1
    print(sum(nums[int(l):int(r)+1]))