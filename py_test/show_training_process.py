#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import configparser
from pla import Perceptron


def main():
    
    df = pd.read_csv('./iris.data',header=None)
    df.tail();

    y = df.iloc[0:99, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:99, [0,2]].values

    ppn = Perceptron(eta=0.1, n_iter=10) 
    #training data
    ppn.fit(X,y)
    weight="%s" % (ppn.get_w())
    print(weight)

    #save weight to file
    config = configparser.ConfigParser()
    config['DEFAULT']['weight'] = weight    # update

    with open('FILE.INI', 'w') as configfile:    # save
        config.write(configfile)

    #plot 
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of misclassifications')
    plt.show()
 
print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
