from collections import deque
def solution(arr):
    stack=[arr[0]]
    arr=deque(arr)
    while arr:
        if stack[-1]==arr[0]:
            arr.popleft()
        else:
            stack.append(arr.popleft())
    return stack

def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a