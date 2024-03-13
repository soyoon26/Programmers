def solution(n):
    word='수박'
    if n%2:
        answer=word*(n//2)+'수'
    else:
        answer=word*(n//2)
    return answer