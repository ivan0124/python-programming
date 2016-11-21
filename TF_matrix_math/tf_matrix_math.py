#!/usr/bin/python

'''
HelloWorld example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import tensorflow as tf

# Start tf session
sess = tf.Session()

# Run the op
#test --> y_data = tf.matmul(x_data, W)+b
x_data=[[1.,1.],
        [2.,2.],
        [3.,3.]]
W=[[1.],
   [2.]]

b=[[1.],
   [2.],
   [3.]]

y_data = tf.matmul(x_data, W)+b

print ("y_data=%s" % sess.run(y_data))
