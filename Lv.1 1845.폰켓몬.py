
def solution(nums):
    answer =0
    monster ={}
    for i in nums:
        if i in monster:
            monster[i] += 1
        else:
            monster[i] = 1
    if len(monster )>=len(nums)//2:
        answer =len(nums )//2
    else:
        answer =len(monster)

    return answer

def solution(ls):
    return min(len(ls)/2, len(set(ls)))