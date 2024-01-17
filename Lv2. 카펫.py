def solution(brown, yellow):
    answer=[]
    ans=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            answer.append([i+2,int(yellow/i)+2])
    for j in range(len(answer)):
        if answer[j][0]+answer[j][1] == int(brown/2)+2 and answer[j][0]>=answer[j][1]:
            ans.append(answer[j][0])
            ans.append(answer[j][1])
    return ans
#짧게
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1): #약수 구하기
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2] #리스트에 추가하지 않고 바로 리턴
#근의 공식 사용
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]
#-b(+-)math.sqrt(b**2-4ac)/2a