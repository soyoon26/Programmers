from collections import deque
def solution(progresses, speeds):
    cnt=0
    progresses=deque(progresses)
    speeds=deque(speeds)
    answer=[]
    while progresses:
        cnt=0
        while progresses[0]<100:
            for i in range(len(progresses)):
                progresses[i]+=speeds[i]
        while progresses[0]>=100:
            progresses.popleft()
            speeds.popleft()
            cnt+=1
            if len(progresses)==0:
                break
        answer.append(cnt)
    return answer


#간결한 코드
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # 100이 되기에 필요한 시간
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1 #걸리는 시간이 작으면 더해주기
    return [q[1] for q in Q]

#깔끔한 코드
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count) #새로 시작
                count = 0
            time += 1
    answer.append(count)
    return answer