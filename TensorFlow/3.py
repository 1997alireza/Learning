import os
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

b = tf.Variable(tf.zeros(5,), name='b')
w = tf.Variable(tf.random_uniform((10, 5), -1, 1), name='w')
x = tf.placeholder(tf.float32, (5, 10))
prediction = tf.nn.softmax(tf.matmul(x, w) + b)
label = tf.placeholder(tf.float32, [None, 5])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(label * tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(.5).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(b))

for i in range(1000):
    # batch_x, batch_label = data.next_batch()
    batch_x = np.random.random_sample((5, 10))
    batch_label = np.random.random_sample((5, 5))
    sess.run(train_step, feed_dict={x: batch_x, label: batch_label})

print(sess.run(b))
sess.close()
