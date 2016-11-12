#!/usr/bin/python

import tensorflow as tf
import numpy as np

# Data sets
IRIS_TRAINING = "iris_training.csv"
IRIS_TEST = "iris_test.csv"

# Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TRAINING, target_dtype=np.int)
test_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TEST, target_dtype=np.int)

x_train, x_test, y_train, y_test = training_set.data, test_set.data, \
  training_set.target, test_set.target

# Build random forest model.
hparams = tf.contrib.tensor_forest.python.tensor_forest.ForestHParams(
        num_trees=3, max_nodes=1000, num_classes=3, num_features=4)
classifier = tf.contrib.learn.TensorForestEstimator(hparams)

# Fit model.
classifier.fit(x=x_train, y=y_train, steps=100)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=x_test, y=y_test, steps=10)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new flower samples.
new_samples = np.array(
    [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
y = classifier.predict(new_samples)
print ('Predictions: {}'.format(str(y)))
