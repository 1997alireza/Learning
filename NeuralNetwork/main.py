import numpy as np
from nn import *
from test_training import test_fixed_function
from matplotlib import pyplot as plt

"""
the data:
        m1: 3   2   4   3   3.5 2   5.5 1   4.5
        m2: 1.5 1   1.5 1   .5  .5  1   1   1
    target: 1   0   1   0   1   0   1   0   ?
"""

if __name__ == '__main__':
    points = [[3, 1.5, 1],
            [2, 1, 0],
            [4, 1.5, 1],
            [3, 1, 0],
            [3.5, .5, 1],
            [2, .5, 0],
            [5.5, 1, 1],
            [1, 1, 0]]
    mystery = [4.5, 1]

    def nn_function(m1, m2, w1, w2, b): return sigmoid(m1 * w1 + m2 * w2 + b)

    def cost_slop_nn(points, w1, w2, b):
        w1_s, w2_s, b_s = [0] * 3
        for point in points:
            z = w1 * point[0] + w2 * point[1] + b
            dsigmoid_dz = sigmoid_derivation(z)
            dc_dz = 2 * (sigmoid(z) - point[2]) * dsigmoid_dz
            dz_dw1 = point[0]
            dz_dw2 = point[1]
            dz_db = 1
            w1_s += dc_dz * dz_dw1
            w2_s += dc_dz * dz_dw2
            b_s += dc_dz * dz_db
        return w1_s, w2_s, b_s

    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()

    c = 0
    for point in points:
        c += cost(nn_function(point[0], point[1], w1, w2, b), point[2])
    c /= len(points)
    print('function: w1 = {0}, w2 = {1}, b = {2}'.format(w1, w2, b), ' cost =', c, '\n')

    # training loop
    for r in range(50000):
        w1_s, w2_s, b_s = cost_slop_nn(points, w1, w2, b)
        w1 -= .01 * w1_s
        w2 -= .01 * w2_s
        b -= .01 * b_s
        c = 0
        for point in points:
            c += cost(nn_function(point[0], point[1], w1, w2, b), point[2])
        c /= len(points)
        if r % 1000 == 0:
            print('function: w1 = {0}, w2 = {1}, b = {2}'.format(w1, w2, b), ' cost =', c, '\n')

    # test
    answer = nn_function(mystery[0], mystery[1], w1, w2, b)
    print(answer)
