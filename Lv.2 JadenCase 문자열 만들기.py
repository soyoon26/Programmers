# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

def solution(s):
    answer = s.lower()
    ans = ''
    ans += s[0].upper()
    for i in range(1, len(answer)):
        if answer[i - 1] == ' ':
            print(answer[i])
            if not answer[i].isdigit():
                ans += answer[i].upper()
                print(ans, "왜")
            else:
                ans += answer[i]
        else:
            ans += answer[i]

    return ans

#공백이 많거나 공백이 제일 앞에 있을 때도 생각해야 한다. title 함수도 존재