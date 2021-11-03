## Emery Chou##

def solution(S, P, Q):
    factor = {'A':1,'C':2,'G':3,'T':4}
    fac = [factor[i] for i in S]
    result = [min(fac[P[i]:Q[i]+1]) for i in range(len(P))]
    return result
