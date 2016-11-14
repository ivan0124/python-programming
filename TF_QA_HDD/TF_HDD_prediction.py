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

# Build random forest model.
hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
        num_trees=train_num_trees, max_nodes=train_max_nodes, num_classes=train_classes_num, num_features=train_feature_num)
classifier = tf.contrib.learn.TensorForestEstimator(hparams, model_dir='./model.ckpt')

# Classify two new HDD samples.
new_samples = np.array(
    [[97170872,0,47,2576,52386013778,22653,0,47,60,0,12,462175,26,0,0,0], [0,565,14,0,0,30433,0,14,0,0,1032,1032,25,0,0,0]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))
