def solution(K, tangerine):
    tan_cnt=dict()
    for i in tangerine:
        if i in tan_cnt:
            tan_cnt[i]+=1
        else:
            tan_cnt[i]=1
    lst=[]
    for j in tan_cnt.values():
        lst.append(j)
    lst.sort(reverse=True)
    ans=0
    for k in lst:
        K=K-k
        ans+=1
        if K<=0:
            break
    return ans

# collections.Counter 사용
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