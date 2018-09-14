import os
import tensorflow as tf
import random
import numpy as np
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def generate_dataset():
    x_batch = np.linspace(-1, 1, 101)
    y_batch = 2 * x_batch + np.random.rand(*x_batch.shape)
    return x_batch, y_batch


def linear_regression():
    x = tf.placeholder(tf.float32, shape=(None,), name='x')
    y = tf.placeholder(tf.float32, shape=(None,), name='y')

    with tf.variable_scope('lreg'):
        w = tf.Variable(np.random.normal(), name='w')
        b = tf.Variable(np.random.normal(), name='b')
        y_pred = tf.multiply(x, w) + b

        loss = tf.reduce_mean(tf.square(y_pred - y))

    return x, y, y_pred, loss


if __name__ == '__main__':
    x_batch, y_batch = generate_dataset()
    x, y, y_pred, loss = linear_regression()
    optimizer = tf.train.GradientDescentOptimizer(.1).minimize(loss)

    with tf.Session() as session:
        session.run(tf.global_variables_initializer())

        for _ in range(100):
            loss_val, _ = session.run([loss, optimizer], {x: x_batch, y: y_batch})
            print('loss: ', loss_val)

        y_pred_batch = session.run(y_pred, {x: x_batch})

    plt.figure(2)
    plt.scatter(x_batch, y_batch)
    plt.plot(x_batch, y_pred_batch)
    plt.show()
