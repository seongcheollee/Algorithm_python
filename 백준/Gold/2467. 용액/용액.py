n = int(input())
nums = list(map(int, input().split()))

l = 0
r = n - 1

ans  = abs(nums[l] + nums[r])
al = l
ar = r

while l < r:

    # 두 용액의 값
    temp = nums[l] + nums[r]

    # 0에 가까우면
    if abs(temp) < ans:
        al = l
        ar = r
        ans = abs(temp)

        if ans == 0:
            break

    if temp < 0:
        l += 1
    else:
        r -= 1

print(nums[al], nums[ar])