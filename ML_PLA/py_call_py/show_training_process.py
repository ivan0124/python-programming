#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import configparser
from pla import Perceptron


def main():
    
    df = pd.read_csv('./iris.data',header=None)
    df.tail();

    y = df.iloc[0:99, 2].values
    y = np.where(y == 'Normal', -1, 1)
    X = df.iloc[0:99, [0,1]].values

    ppn = Perceptron(eta=0.3, n_iter=10) 
    #training data
    ppn.fit(X,y)
    W=ppn.get_w()

    weight=''
    for v in W:
        weight+=str(v)
        weight+=','

    weight=weight[:-1]
    print("fit weight = %s" % (weight))

    #save weight to file
    config = configparser.ConfigParser()
    config['DEFAULT']['weight'] = weight

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
