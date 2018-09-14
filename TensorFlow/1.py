import os
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('hello')

# A session allows to execute graphs or part of graphs. It allocates resources.
sess = tf.Session()
print(sess.run(hello))
print(tf.constant(23) + tf.constant(9))
print(sess.run(tf.constant(23) + tf.constant(9)))
sess.close()
