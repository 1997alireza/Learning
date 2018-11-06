import numpy as np


LEARNING_RATE = 1e-4


def gradient_decent_unit(x, y, beta):
    # gradient of any quadratic function, such as our cost function
    grad = np.matmul(x.T, (np.matmul(x, beta) - y))
    return grad / np.linalg.norm(grad)


def lr_batch(x, y):
    beta = np.random.normal(.5, .5, (x.shape[1],))

    for _ in range(100000):
        beta -= LEARNING_RATE * gradient_decent_unit(x, y, beta)
    return beta


if __name__ == '__main__':
    data = np.load('data.npz')
    x1 = np.array(data['x1'])
    x2 = np.array(data['x2'])
    y = np.array(data['y'])

    x = np.zeros((x1.shape[0], 3))
    x[:, 0] = np.ones((x1.shape[0]))
    x[:, 1] = x1
    x[:, 2] = x2
    print(lr_batch(x, y))
