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
train_model_dir='./model.ckpt'


# Load datasets.
ipd = pd.read_csv("./HDD_SMART_DATA.csv")

# Shuffle datasets
shuffled = ipd.sample(frac=1)
x_test_sample_num = int(len(shuffled) * test_sample_rate)
x_train = shuffled.values[0:len(shuffled)- x_test_sample_num, train_feature_column]
y_train = shuffled.values[0:len(shuffled)- x_test_sample_num, train_label_column]
x_test = shuffled.values[len(shuffled)- x_test_sample_num:, train_feature_column]
y_test = shuffled.values[len(shuffled)- x_test_sample_num:, train_label_column]

# Change datasets value type to float
x_train=x_train.astype(np.float)
x_test=x_test.astype(np.float)
y_train=y_train.astype(np.float)
y_test=y_test.astype(np.float)

# Build random forest model.
hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
        num_trees=train_num_trees, max_nodes=train_max_nodes, num_classes=train_classes_num, num_features=train_feature_num)
classifier = tf.contrib.learn.TensorForestEstimator(hparams)

# Fit model.
classifier.fit(x=x_train, y=y_train, steps=train_steps)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=x_test, y=y_test)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))


# Classify two new HDD samples.
new_samples = np.array(
    [[97170872,0,47,2576,52386013778,22653,0,47,60,0,12,462175,26,0,0,0], [0,565,14,0,0,30433,0,14,0,0,1032,1032,25,0,0,0]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))
