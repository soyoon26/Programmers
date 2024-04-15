from itertools import permutations
import math

def solution(numbers):
    nums = list(numbers)
    lst = []
    for i in range(1, len(nums) + 1):
        num = list(''.join(map(str, per)) for per in permutations(nums, i))
        lst.extend(num)
    lst = [int(x) for x in lst]
    lst = set(lst)

    def prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    cnt = 0
    for j in lst:
        if prime(j):
            cnt += 1

    return cnt

# 다른 방법 
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)