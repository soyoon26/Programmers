def solution(n):
    num=[0,1]
    for i in range(2,n+1):
        num+=[num[i-2]+num[i-1]]
    answer=num[n]%1234567
    return answer

#개편이전 풀이방법
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b #동시할당이라 가능
    return a