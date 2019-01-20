import numpy as np
import tensorflow as tf
from active_function import *
import pandas as pd


class DrinksNN_TF:
    def __init__(self, layer_dim=None, h_active_function=tanh, o_active_function=softmax):
        """

        :param h_active_function: hidden layers active function, get input as a number
        :param o_active_function: output layer active function, get input as a numpy array
        """
        if layer_dim is None:
            layer_dim = [13, 8, 5, 3]
            # using 2 hidden layers:
            #  input layer: 13 neurons
            #  1st hidden layer: 8 neurons
            #  2nd hidden layer: 5 neurons
            #  output layer: 3 neurons
        self.layer_dim = layer_dim
        self.h_active_function = h_active_function
        self.o_active_function = o_active_function

        self.x = tf.placeholder("float", shape=[None, self.layer_dim[0]])
        self.y = tf.placeholder("float", shape=[None, self.layer_dim[-1]])

        self.w = []
        for i in range(len(self.layer_dim) - 1):
            w_shape = (layer_dim[i], layer_dim[i + 1])
            self.w.append(tf.Variable(tf.random_normal(w_shape, stddev=0.1)))

        # Forward propagation
        h = tf.nn.tanh(tf.matmul(self.x, self.w[0]))
        for layer_id in range(1, len(self.layer_dim) - 2):  # hidden layers
            h = tf.nn.tanh(tf.matmul(h, self.w[layer_id]))
        self.y_hat = tf.nn.softmax(tf.matmul(h, self.w[-1]))
        self.predict = tf.argmax(self.y_hat, axis=1)
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def train(self, x_batch, y_batch, learning_rate=.7, epoch_num=100):
        assert type(x_batch) == type(y_batch) == list and len(x_batch) == len(y_batch) > 0 \
               and len(x_batch[0]) == self.layer_dim[0] and len(y_batch[0]) == self.layer_dim[-1], 'invalid input'

        cost = tf.losses.mean_squared_error(labels=self.y, predictions=self.y_hat)
        # cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=yhat))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        updater = optimizer.minimize(cost)

        for epoch in range(epoch_num):
            self.sess.run(updater, feed_dict={self.x: x_batch, self.y: y_batch})
            epoch_accuracy = np.mean(np.argmax(y_batch, axis=1) ==
                                     self.sess.run(self.predict, feed_dict={self.x: x_batch, self.y: y_batch}))
            print('Accuracy on epoch {}: {}'.format(epoch, epoch_accuracy))

    def test(self, x):
        assert type(x) == list and len(x) == self.layer_dim[0], 'invalid input'
        return self.sess.run(self.predict, feed_dict={self.x: [x]})


if __name__ == '__main__':
    dataset = pd.read_csv('datasets/Drinks.csv')
    features = dataset.iloc[:, :13].values.tolist()
    outputs = dataset.iloc[:, 13:].values.tolist()

    model = DrinksNN_TF()
    model.train(features, outputs)

    print(model.test(features[10])[0])
    print(np.argmax(outputs[10]))
    print(model.test(features[120])[0])
    print(np.argmax(outputs[120]))
    print(model.test(features[44])[0])
    print(np.argmax(outputs[44]))
    print(model.test(features[160])[0])
    print(np.argmax(outputs[160]))

