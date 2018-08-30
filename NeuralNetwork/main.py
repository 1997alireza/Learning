from math import exp


def neural_network_functor(m1, m2, w1, w2, b):
    return sigmoid(m1*w1 + m2*w2 + b)


def sigmoid(x):
    return 1 / (1 + exp(-x))

