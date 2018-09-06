from math import exp


def fixed_function(b):
    return b


def linear_function(m, w, b):
    return m*w + b


def nn_function(m1, m2, w1, w2, b):
    return sigmoid(m1*w1 + m2*w2 + b)


def sigmoid(x):
    return 1 / (1 + exp(-x))


def cost(prediction, target):
    return (prediction - target) ** 2


def cost_slop_fixed(prediction, target):
    h = .00001
    return (cost(prediction + h, target) - cost(prediction, target)) / h


def cost_slop_linear(m_list, t_list, w, b):
    w_slop = 0
    b_slop = 0
    for i, m in enumerate(m_list):
        w_slop += 2 * (linear_function(m, w, b) - t_list[i]) * m
        b_slop += 2 * (linear_function(m, w, b) - t_list[i]) * 1
    return w_slop, b_slop
