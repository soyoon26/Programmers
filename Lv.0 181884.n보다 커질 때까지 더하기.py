def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer+=i
        print(answer)
        if answer > n:
            return answer
