def solution(people, limit):
    answer = 0
    people.sort()
    front=0
    end=len(people)-1
    while front <= end:
        if people[front]+people[end]<=limit:
            answer+=1
            front+=1
            end-=1
        else:
            answer+=1
            end-=1
    return answer
#겹치는 사람들을 빼는 법
# def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer