from collections import deque
def solution(n, words):
    answer = 0
    words=deque(words)
    stack=[words.popleft()]
    for i in range(len(words)):
        if words[i][0] == stack[-1][-1] and words[i] not in stack:
            stack.append(words[i])
        else:
            answer=len(stack)+1
            break
    result=[0,0]
    if answer != 0:
        if answer%n:
            result=[answer%n,answer//n+1]
        else:
            result=[n,answer//n]
    return result
#숏코딩
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]