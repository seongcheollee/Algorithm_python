def solution(numbers, target):

    def dfs(sum_n, depth):
        res = 0
        # 종료조건
        if depth == len(numbers):
            if sum_n == target:
                return 1
            else:
                return 0
        # 탐색
        else:
            res += dfs(sum_n + numbers[depth], depth+1)
            res += dfs(sum_n - numbers[depth], depth+1)
            return res
        
    return dfs(0,0)