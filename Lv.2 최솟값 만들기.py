def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer
#큰 숫자는 제일 작은 숫자와 곱해지게 정렬하기