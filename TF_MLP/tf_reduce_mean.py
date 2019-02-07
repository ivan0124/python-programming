#!/usr/bin/python

import tensorflow as tf
 
x=tf.constant([[1.0,2.0,3.0],[1.0,2.0,3.0],[1.0,2.0,3.0]])
print(x)

with tf.Session() as sess:
    print("x=")
    print(sess.run(x))
    #Total mean: [(1+2+3 + 1+2+3 + 1+2+3)/9] = [2]
    print("Total mean ==> reduce_mean(x)=")
    print(sess.run(tf.reduce_mean(x)))
    #raw sum: [(1+1+1)/3, (2+2+2)/3, (3+3+3)/3] = [1, 2, 3]
    print("Raw(axis=0) mean ==> reduce_mean(x,0)=")
    print(sess.run(tf.reduce_mean(x,0)))
    #column sum: [(1+2+3)/3, (1+2+3)/3, (1+2+3)/3] = [2, 2, 2]
    print("Column(axis=1) mean ==> reduce_mean(x,1)=")
    print(sess.run(tf.reduce_mean(x,1)))
