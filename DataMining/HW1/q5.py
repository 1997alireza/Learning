import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pandas as pd

LEARNING_RATE = 1e-5
ITERATIONS = 15000000


def gradient_decent_unit(x, y, beta):
    # gradient of any quadratic function, such as our cost function
    grad = np.matmul(x.T, (np.matmul(x, beta) - y))
    norm = np.linalg.norm(grad)
    if norm == 0:
        return grad, True
    return grad / norm, False


def lr_batch(x, y):
    beta = np.random.normal(.5, .5, (x.shape[1], 1))
    y = np.reshape(y, (-1, 1))

    for _ in range(ITERATIONS):
        grad, stop = gradient_decent_unit(x, y, beta)
        if stop:
            return beta
        beta -= LEARNING_RATE * grad
    return beta


def lr_stochastic(x, y):
    beta = np.random.normal(.5, .5, (x.shape[1], 1))

    for _ in range(ITERATIONS):
        random_index = random.randint(0, np.shape(x)[0] - 1)
        x = np.reshape(x[random_index], (1, -1))
        y = np.reshape(y[random_index], (1, 1))
        grad, _ = gradient_decent_unit(x, y, beta)
        beta -= LEARNING_RATE * grad
    return beta


if __name__ == '__main__':
    data = np.load('data.npz')
    x1 = np.array(data['x1'])
    x2 = np.array(data['x2'])
    y = np.array(data['y'])

    x = np.zeros((x1.shape[0], 4))
    x[:, 0] = np.ones((x1.shape[0]))
    x[:, 1] = x1
    x[:, 2] = x2 ** 2
    x[:, 3] = x2 ** 2 * x1
    beta = lr_stochastic(x, y)
    beta = beta.reshape(4)
    print('beta:\n', beta)

    predict = np.matmul(x, beta)
    train_error = np.linalg.norm(predict - y)
    print('train error: ', train_error)

    x1_test = np.array(data['x1_test'])
    x2_test = np.array(data['x2_test'])
    y_test = np.array(data['y_test'])

    x_test = np.zeros((x1_test.shape[0], 4))
    x_test[:, 0] = np.ones((x1_test.shape[0]))
    x_test[:, 1] = x1_test
    x_test[:, 2] = x2_test ** 2
    x_test[:, 3] = x2_test ** 2 * x1_test
    predict_test = np.matmul(x_test, beta)
    test_error = np.linalg.norm(predict_test - y_test)
    print('test error: ', test_error)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(x1_test, x2_test, y_test, marker='o')
    ax.scatter(x1_test, x2_test, (np.matmul(x_test, beta)).tolist(), marker='x')
    plt.show()
