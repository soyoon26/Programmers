from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        cnt = 0
        price = prices.popleft()
        for i in prices:
            if price <= i:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    return answer