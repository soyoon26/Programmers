def solution(s):
    zero=[]
    cnt=0
    while len(s) != 1:
        num=0
        for i in s:
            if i == '0':
                zero.append('0')
            else:
                num+=1
        cnt+=1
        s=bin(num)[2:]
    answer=[cnt,len(zero)]
    return answer

#시간 단축코드
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]