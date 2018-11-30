from math import log
import numpy as np


def entropy(*counts):
    total = sum(c for c in counts)
    ent = 0
    for c in counts:
        p = c / total
        if p != 0:
            ent -= p * log(p, 2)
    return ent


def norm2_error(y_real, y_predict):
    if type(y_real) == list:
        y_real = np.array(y_real)
        y_predict = np.array(y_predict)

    return np.linalg.norm(y_real - y_predict)
