def solution(n, lost, reserve):
    lst=set(lost)
    rsv=set(reserve)
    mid=lst&rsv
    lst=lst-mid
    rsv=rsv-mid
    for i in rsv:
        if i-1 in lst:
            lst.remove(i-1)
        elif i+1 in lst:
            lst.remove(i+1)
    return n-len(lst)