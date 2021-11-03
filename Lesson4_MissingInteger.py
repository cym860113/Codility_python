## Emery Chou ##
def solution(A):    
    val = max(A)
    if val <= 0:
        return 1
    else:
        for i in range(1,val+1):
            if i not in A:
                return i
        return val+1
