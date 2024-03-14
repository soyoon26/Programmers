def solution(s):
    s=list(s)
    s.sort(reverse=True)
    answer=''
    for i in s:
        answer+=i
    return answer

#간결한 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))