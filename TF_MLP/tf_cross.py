#!/usr/bin/python

import tensorflow as tf
 
#our NN's output
logits=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])

y=tf.constant([[2.0,2.0,2.0],[3.0,3.0,3.0],[4.0,4.0,4.0]])
a =  y*logits

with tf.Session() as sess:
    logits_=sess.run(logits)
    y_=sess.run(y)
    a_ = sess.run(a)
    print("logits=")
    print(logits_)
    #
    print("y=")
    print(y_)
    #
    print("y*logits=")
    print(a_)
