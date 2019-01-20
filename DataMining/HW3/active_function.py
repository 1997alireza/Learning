import numpy as np


def tanh(x, derived=False):
    tanh_x = np.tanh(x)
    if derived:
        return 1 - tanh_x * tanh_x
    return tanh_x


def softmax(x, derived=False):
    sm = np.exp(x) / np.sum(np.exp(x), axis=0)
    if derived:
        derived_vec = np.zeros(np.shape(x))
        for i in range(len(derived_vec)):
            for j in range(i, len(derived_vec)):
                derived_vec[i] += sm[i] * (1 - sm[i]) if i == j else -sm[i] * sm[j]
        return derived_vec
    return sm
