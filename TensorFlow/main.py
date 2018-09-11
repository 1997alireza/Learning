import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('hello')
sess = tf.Session()
print(sess.run(hello))
print(sess.run(tf.constant(23) + tf.constant(9)))
sess.close()