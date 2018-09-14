import os
import tensorflow as tf
import random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# f = sigmoid(m1*w1 + m2*w2 + b)

points = [[3, 1.5, 1],
          [2, 1, 0],
          [4, 1.5, 1],
          [3, 1, 0],
          [3.5, .5, 1],
          [2, .5, 0],
          [5.5, 1, 1],
          [1, 1, 0]]

mystery = [4.5, 1]

b = tf.Variable(random.random(), name='b')
w1 = tf.Variable(random.random(), name='w1')
w2 = tf.Variable(random.random(), name='w2')
m1 = tf.placeholder(tf.float32, name='m1')
m2 = tf.placeholder(tf.float32, name='m2')

prediction = tf.sigmoid(tf.add(tf.add(tf.multiply(m1, w1), tf.multiply(m2, w2)), b))
label = tf.placeholder(tf.float32)

cost = tf.losses.mean_squared_error(label, prediction)

train_op = tf.train.RMSPropOptimizer(.9, .9).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    for point in points:
        sess.run([cost, train_op], feed_dict={m1: point[0], m2: point[1], label: point[2]})
print(sess.run(prediction, feed_dict={m1: points[0][0], m2: points[0][1]}))
# it returns between 0.99999 and 1

sess.close()
