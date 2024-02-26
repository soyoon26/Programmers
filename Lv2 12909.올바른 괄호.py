def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        elif i==')' and stack:
            stack.pop()
        elif i==')' and len(stack)==0:
            answer=False
    if stack:
        answer=False
    return answer

def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0