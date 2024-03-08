def solution(answers):
    answer = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    def score(lst):
        my_score=0
        for i in range(len(answers)):
            if lst[i%len(lst)] == answers[i]:
                my_score+=1
        return my_score
    one_score=score(one)
    two_score=score(two)
    three_score=score(three)
    lst=[one_score,two_score,three_score]
    if one_score == max(lst):
        answer.append(1)
    if two_score == max(lst):
        answer.append(2)
    if three_score == max(lst):
        answer.append(3)
    return answer