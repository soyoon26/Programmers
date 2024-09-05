def solution(s):
    word=''
    answer = []
    for i in range(len(s)):
        if s[i] not in word:
            answer.append(-1)
        else:
            answer.append(word[::-1].index(s[i])+1)
        word+=s[i]
        
    return answer
