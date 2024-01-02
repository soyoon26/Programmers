# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    ans1 = 1
    ans2 = 0
    for i in num_list:
        ans1 *= i
        ans2 += i
    if ans1 > ans2**2 :
        answer = 0
    else :
        answer = 1
    return answer