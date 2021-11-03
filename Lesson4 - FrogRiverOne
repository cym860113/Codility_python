### Emery Chou ###


def solution(X, A):
    B = [i for i in range(1,X+1)]
    for time,i in enumerate(A):
        if i in B:B.remove(i)
        if len(B) == 0:
            return time
    return -1
