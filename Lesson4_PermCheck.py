## EmeryChou ##

def solution(A):
    my_set = set()

    for i in range(1, len(A)+1):
        my_set.add(i)
    for i in A:
        if i in my_set:
            my_set.remove(i)
    if my_set == set():
        return 1
    else:return 0
