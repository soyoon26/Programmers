def solution(arr):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    for i in range(len(arr) - 1):
        arr[i + 1] = arr[i] * arr[i + 1] / gcd(arr[i], arr[i + 1])
    return arr[-1]


#모듈사용
from fractions import gcd
def nlcm(num):
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)
    return answer
print(nlcm([2,6,8,14]));