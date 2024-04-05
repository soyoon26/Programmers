def solution(K, tangerine):
    dict_tan = dict()

    for i in tangerine:
        if i in dict_tan:
            dict_tan[i] += 1
        else:
            dict_tan[i] = 1
    tan = []
    for v in dict_tan.values():
        tan.append(v)
    tan.sort(reverse=True)

    sum_t = 0
    for t in range(len(tan)):
        sum_t += tan[t]
        if sum_t >= K:
            ans = t + 1
            break
    return ans


# collections의 Counter사용
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer

# list 사용, dict사용하지 말고 인덱스 이용
def solution(k, tangerine):
    answer = 0
    l = [0 for i in range(max(tangerine))]
    for i in range(len(tangerine)):
        l[tangerine[i]-1] += 1
    l.sort(reverse = True)

    index = 0
    while answer<k:
        answer += l[index]
        index += 1
    return index