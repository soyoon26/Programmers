from collections import defaultdict


def solution(name, yearning, photo):
    answer = []
    score = defaultdict(int)
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for i in photo:
        total = 0
        for j in i:
            total += score[j]
        answer.append(total)

    return answer