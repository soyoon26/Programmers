# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
#
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(s):
    answer = 0
    p=['()','[]','{}']
    for i in range(len(s)):
        s+=s[0]
        s=s[1:]
        s_lst=s
        while p[0] in s_lst or p[1] in s_lst or p[2] in s_lst:
            s_lst=s_lst.replace(p[0],'')
            s_lst=s_lst.replace(p[1],'')
            s_lst=s_lst.replace(p[2],'')
        if len(s_lst) == 0: #다 없어진 것이라면 더해주기
            answer+=1
    return answer

#스택으로 다시 풀기