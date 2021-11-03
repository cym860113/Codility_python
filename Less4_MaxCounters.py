##Emery Chou##

def solution(N, A):
  Final = [0]*N

  for idx,i in enumerate(A):
      if i>N:
          Final = [max(Final)]*N
      else:
          Final[i-1] += 1
  return Final
