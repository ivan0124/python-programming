#!/usr/bin/python

import csv
import tensorflow as tf
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, shutil
from tensorflow.python.framework import graph_util

#clear history log
folder = './logs'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

#load iris.csv data
ipd = pd.read_csv("./iris.csv")
ipd.head()

species = list(ipd['Species'].unique())
ipd['One-hot'] = ipd['Species'].map(lambda x: np.eye(len(species))[species.index(x)] )
#print ("ipd.sample(5)=\n%s" % (ipd.sample(5)))

#split the data into training and test sets
shuffled = ipd.sample(frac=1)
trainingSet = shuffled[0:len(shuffled)-50]
testSet = shuffled[len(shuffled)-50:]
#train = trainingSet.sample(50)
#print ("train=\n%s" % (train))

# Parameters
learning_rate = 0.001
training_epochs = 100
#batch_size = 50
#display_step = 1

# Network Parameters
n_hidden_1 = 256 # 1st layer number of features
n_hidden_2 = 128 # 2nd layer number of features
n_hidden_3 = 64 # 3rd layer number of features
n_hidden_4 = 128 # 4th layer number of features
n_input = 4 # Iris data input (img shape: 1*4)
n_classes = 3 # Iris total 3 classes

# tf Graph input
with tf.name_scope('input_data'):
    inp = tf.placeholder(tf.float32, [None, n_input])
with tf.name_scope('OneHot_label'):
    y_ = tf.placeholder(tf.float32, [None, n_classes])


# Create model
def multilayer_perceptron(x):
# Store layers weight & bias
    with tf.name_scope('weight'):
        weights = {
            'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
            'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
            'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
            'h4': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_4])),
            'out': tf.Variable(tf.random_normal([n_hidden_4, n_classes]))
        }
    with tf.name_scope('bias'):
        biases = {
            'b1': tf.Variable(tf.random_normal([n_hidden_1])),
            'b2': tf.Variable(tf.random_normal([n_hidden_2])),
            'b3': tf.Variable(tf.random_normal([n_hidden_3])),
            'b4': tf.Variable(tf.random_normal([n_hidden_4])),
            'out': tf.Variable(tf.random_normal([n_classes]))
        }
    # Hidden layer1 with RELU activation
    with tf.name_scope('layer1'):
        layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
        layer_1 = tf.nn.relu(layer_1)
    # Hidden layer2 with RELU activation
    with tf.name_scope('layer2'):
        layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
        layer_2 = tf.nn.relu(layer_2)
    # Hidden layer3 with RELU activation
    with tf.name_scope('layer3'):
        layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
        layer_3 = tf.nn.relu(layer_3)
    # Hidden layer4 with RELU activation
    with tf.name_scope('layer4'):
        layer_4 = tf.add(tf.matmul(layer_3, weights['h4']), biases['b4'])
        layer_4 = tf.nn.relu(layer_4)
    # Output layer with linear activation
    with tf.name_scope('output_layer'):
        out_layer = tf.matmul(layer_4, weights['out']) + biases['out']
    return out_layer


# Define MLP network model
with tf.name_scope('MLP'):
    y = multilayer_perceptron(inp)

# Define loss
with tf.name_scope('softmax_cross_entropy_with_logits'):
    cross_entropy=tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=y_)
with tf.name_scope('total_loss'):
    loss = tf.reduce_sum(cross_entropy)
    tf.summary.scalar('total_loss', loss)

#Define Optimizer
with tf.name_scope('Optimizer'):
    train_step= tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)


# Launch the graph
with tf.Session() as sess:
# Merge all the summaries and write them out to ./train
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter('./logs',sess.graph)
    
# Initializing the variables
    init = tf.global_variables_initializer() #new function
    sess.run(init)
    # Training cycle
    keys = ['sepal_length', 'sepal_width','petal_length', 'petal_width']
    for epoch in range(training_epochs):
        train = trainingSet.sample(50)
        summary, predict_value = sess.run([merged, train_step], feed_dict={inp: [x for x in train[keys].values],
                                         y_: [x for x in train['One-hot'].as_matrix()]})
        train_writer.add_summary(summary, epoch)

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print ("=accuracy=\n%s" % sess.run(accuracy, feed_dict={inp: [x for x in testSet[keys].values], 
                                    y_: [x for x in testSet['One-hot'].values]}))

    # Create file to store pb model
    prediction_labels = tf.argmax(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=y_), axis=1, name="output") # 'output' name is important
    pb_file_path = os.getcwd()
    print(pb_file_path)
    #store model to pb file
    constant_graph = graph_util.convert_variables_to_constants(sess,sess.graph_def, ["output"]) # 'output' name is important
    with tf.gfile.GFile(pb_file_path+'/model.pb', mode='wb') as f:
        f.write(constant_graph.SerializeToString())
    
