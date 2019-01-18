import numpy as np


def tanh(x, derived=False):
    tanh_x = np.tanh(x)
    if derived:
        return 1 - tanh_x * tanh_x
    return tanh_x


def softmax(x, derived=False):
    if derived:
        return 0  # TODO
    return np.exp(x) / np.sum(np.exp(x), axis=0)
