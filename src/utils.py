def max_index(l):
    maxi = 0
    for i in range(0, len(l)):
        if l[i] > l[maxi]:
            maxi = i
    return maxi


def min_index(l):
    mini = 0
    for i in range(0, len(l)):
        if l[i] < l[mini]:
            mini = i
    return mini
