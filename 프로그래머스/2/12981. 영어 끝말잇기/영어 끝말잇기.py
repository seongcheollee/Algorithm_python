#def solution(n, words):

from collections import defaultdict
def solution(n, words):
    dic = defaultdict(int)

    for i, w in enumerate(words):
        if i == 0:
            dic[i % n + 1] += 1
            continue

        dic[i % n + 1] += 1

        if w in words[:i]:
            return [i % n + 1, dic[i % n + 1]]

        if words[i - 1][-1] != w[0]:
            return [i % n + 1, dic[i % n + 1]]

    return [0, 0]
