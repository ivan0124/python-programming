#!/usr/bin/python

import tensorflow as tf
 
x=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])

with tf.Session() as sess:
    print("x=")
    print(sess.run(x))
    #Total sum: [1+2+3 + 1+2+3 + 1+2+3] = [18]
    print("Total sum ==> reduce_sum(x)=")
    print(sess.run(tf.reduce_sum(x)))
    #raw sum: [1+1+1, 2+2+2, 3+3+3] = [3, 6, 9]
    print("Raw sum ==> reduce_sum(x,0)=")
    print(sess.run(tf.reduce_sum(x,0)))
    #column sum: [1+2+3, 1+2+3, 1+2+3] = [6, 6, 6]
    print("Column sum ==> reduce_sum(x,1)=")
    print(sess.run(tf.reduce_sum(x,1)))
