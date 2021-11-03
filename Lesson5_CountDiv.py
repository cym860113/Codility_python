## Emery Chou ##
def solution(A, B, K):
    num = 0
    for i in range(A,B+1):
        num = B//K-A//K
        if A%K==0:
            return num+1
        return num

