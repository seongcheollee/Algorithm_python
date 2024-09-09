def solution(nums):
    n = len(nums) // 2
    s = len(set(nums))

    if s < n:
        return s
    else:
        return n