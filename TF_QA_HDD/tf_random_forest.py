#!/usr/bin/python

import tensorflow as tf
import numpy as np
import pandas as pd

# Load datasets.
ipd = pd.read_csv("./HDD_SMART_DATA.csv")
shuffled = ipd.sample(frac=1)

x_test_sample_num = int(len(shuffled) * 0.3)
print ("x_test_len = %s\n" % (x_test_sample_num))
x_train = shuffled.values[0:len(shuffled)- x_test_sample_num,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
y_train = shuffled.values[0:len(shuffled)- x_test_sample_num,[0]]
x_test = shuffled.values[len(shuffled)- x_test_sample_num:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
y_test = shuffled.values[len(shuffled)- x_test_sample_num:,[0]]

# Build random forest model.
hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
        num_trees=5, max_nodes=1000, num_classes=2, num_features=16)
classifier = tf.contrib.learn.TensorForestEstimator(hparams)

# Fit model.
classifier.fit(x=x_train, y=y_train, steps=300)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=x_test, y=y_test)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new HDD samples.
new_samples = np.array(
    [[97170872,0,47,2576,52386013778,22653,0,47,60,0,12,462175,26,0,0,0], [0,565,14,0,0,30433,0,14,0,0,1032,1032,25,0,0,0]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))
