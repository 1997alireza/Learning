import os
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()
b = tf.Variable(tf.zeros(100,))
w = tf.Variable(tf.random_uniform((748, 100), -1, 1))
x = tf.placeholder(tf.float32, (100, 748))
h = tf.nn.relu(tf.matmul(x, w) + b)
sess.run(tf.global_variables_initializer())
print(sess.run(h, {x: np.random.random_sample((100, 748))}))
sess.close()
