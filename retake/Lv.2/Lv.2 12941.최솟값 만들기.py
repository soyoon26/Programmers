def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum=0
    for i in range(len(A)):
        sum+=A[i]*B[i]
    return sum

# zip 사용가능
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])