#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    
    df = pd.read_csv('./iris.data',header=None)
    df.tail();

    y = df.iloc[0:99, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:99, [0,2]].values
    
    plt.scatter(X[:49, 0], X[:49, 1], color='red', marker='o', label='setosa')
    plt.scatter(X[49:99, 0], X[49:99, 1], color='blue', marker='x', label='versicolor')

    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend(loc='upper left')

    plt.show()

print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
