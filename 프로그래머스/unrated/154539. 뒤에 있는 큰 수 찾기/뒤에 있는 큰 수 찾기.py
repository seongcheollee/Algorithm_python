def solution(numbers):
    stk = []
    res = [-1] * len(numbers)

    for i in range(len(numbers)):
            # 스택에 넣고, 뒤의 값이 해당 값보다 큰 경우 그 값을 넣어줌.
            while stk and numbers[stk[-1]] < numbers[i]:
                res[stk.pop()] = numbers[i]
            stk.append(i)
    
    return res