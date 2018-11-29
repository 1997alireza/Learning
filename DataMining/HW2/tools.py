from math import log


def entropy(*counts):
    total = sum(c for c in counts)
    ent = 0
    for c in counts:
        p = c / total
        if p != 0:
            ent -= p * log(p, 2)
    return ent
