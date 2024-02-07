def solution(n):
    answer = ''
    bin_n = bin(n)
    while answer.count('1') != bin_n.count('1'):
        answer = bin(n + 1)
        n += 1

    return int(answer, 2)