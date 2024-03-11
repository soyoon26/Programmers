def solution(n):
    ans = [0, 1, 2] + [0] * (n - 2)
    for i in range(3, n + 1):
        ans[i] = (ans[i - 1] + ans[i - 2]) % 1234567
    return ans[n]