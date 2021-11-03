## Emery Chou ##
def solution(A):    
    zeros = 0
    passing = 0
    for i in A:
        if i == 0:
            zeros += 1
        else:
            passing += zeros
    return passing
