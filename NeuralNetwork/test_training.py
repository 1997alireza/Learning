import numpy
from nn import *


def test_linear_regression():
    # linear regression
    w = numpy.random.randn()
    b = numpy.random.randn()
    m = [1, 2, 4]
    t = [2, 4, 10]
    c = 0
    for i, mi in enumerate(m):
        c += cost(linear_function(mi, w, b), t[i])
    c /= len(m)
    print('linear function: w = {0}, b = {1}'.format(w, b), ' cost =', c, '\n')

    # training loop
    for _ in range(5000):
        w_s, b_s = cost_slop_linear(m, t, w, b)
        w -= .01 * w_s
        b -= .01 * b_s
        c = 0
        for i, mi in enumerate(m):
            c += cost(linear_function(mi, w, b), t[i])
        c /= len(m)
        print('linear function: w = {0}, b = {1}'.format(w, b), ' cost =', c, '\n')


def test_fixed_function():
    # nn function : f = b
    # target is 4
    b = numpy.random.randn()
    t = 4
    c = cost(fixed_function(b), t)
    print("function's value =", fixed_function(b), "  cost =", c, '\n')

    # training loop
    while c > .0001:
        b -= .1 * cost_slop_fixed(fixed_function(b), t)
        c = cost(fixed_function(b), t)
        print("function's value =", fixed_function(b), "  cost =", c, '\n')


if __name__ == '__main__':
    test_fixed_function()
