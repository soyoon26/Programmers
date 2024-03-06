def solution(n, left, right):
    arr=[]
    for i in range(left//n+1,right//n+2):
        for j in range(i):
            arr.append(i)
        for k in range(i+1,n+1):
            arr.append(k)
    return arr[left%n:len(arr)-(n-right%n)+1]

#몫과 나머지
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer