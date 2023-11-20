def solution(nums):
    a = set(nums)
    if len(nums) // 2 <len(a):
        return len(nums) // 2
    else:
        return len(set(nums))
