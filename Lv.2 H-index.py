# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
#
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

def solution(citations):
    max_h = max(citations)
    answer = 0
    for i in range(max_h, -1, -1):
        count = 0
        for j in range(len(citations)):
            if citations[j] - i >= 0:
                count += 1
        if count >= i:
            answer = i
            break

    print(answer)

    return answer
#반례 6,5,3,3,0 답:3

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
#제일 많은 순으로 정렬하고 1부터 인덱스, 인덱스는 결국 사용되는 횟수
