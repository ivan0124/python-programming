#!/usr/bin/python

import tensorflow as tf
import numpy as np
import pandas as pd

# Train parameters
test_sample_rate = 0.3
train_label_column = [0] 
train_feature_column = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
train_feature_num = len (train_feature_column)
train_classes_num = 2 
train_num_trees=5
train_max_nodes=1000
train_steps=300
train_model_dir='./HDD_prediction_model'


# Load datasets.
ipd = pd.read_csv("./smart.csv")

# Load random forest model.
hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
        num_trees=train_num_trees, max_nodes=train_max_nodes, num_classes=train_classes_num, num_features=train_feature_num)
classifier = tf.contrib.learn.TensorForestEstimator(hparams,model_dir=train_model_dir)


# Classify two new HDD samples.
#for i in range(0,10):
#    new_samples = np.array(ipd.values[i*30:30*(i+1), train_feature_column], dtype=float)
#    y = classifier.predict(new_samples)
#    print ('Predictions: {}'.format(str(y)))
fail_count=0;
for i in range(0,len(ipd)):
    new_samples = np.array(ipd.values[i:i+1, train_feature_column], dtype=float)
    y = classifier.predict(new_samples)
    #print ('Predictions: {}'.format(str(y)))
    if y == 1:
        fail_count += 1
        fail_rate = float(fail_count) / float(i)
        print("y == 1, total count=%s, fail count = %s, fail rate=%s\n" % (i,fail_count, fail_rate))

print("total count=%s, fail count = %s\n" % (i,fail_count))
