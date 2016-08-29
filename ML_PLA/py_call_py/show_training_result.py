#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from pla import Perceptron

def plot_decision_regions(X, y, classifier, resolution=5): 
    markers = ['x', 'o', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'gary', 'cyan']
    print("y=%s" % colors[:len(np.unique(y))])
    cmap = ListedColormap(colors[:len(np.unique(y))])

    print(X.shape)
    print("X = %s" % X)
    #print(enumerate(np.unique(y)))
    print("np.unique(y) = %s" % np.unique(y))
    print("y = %s" % y)
    print("y.shape = %s" % y.shape)
    print(cmap(0))
    #plot the decision surface
    
    x1_min, x1_max = X[:, 0].min()-1, X[:, 0].max()+1
    print("X1_min=%s, x1_max=%s" % (x1_min, x1_max))
    x2_min, x2_max = X[:, 1].min()-1, X[:, 1].max()+1
    print("X2_min=%s, x2_max=%s" % (x2_min, x2_max))


    print("np.arange(x1_min, x1_max, resolution) = %s" % np.arange(x1_min, x1_max, resolution))
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), 
                           np.arange(x2_min, x2_max, resolution))

    print("xx1 = %s" % xx1)
    print("xx2 = %s" % xx2)
    print(xx1.shape)
    print(xx2.shape)
    print("xx1.ravel() = %s" % xx1.ravel())
    print("xx2.ravel() = %s" % xx2.ravel())

    print("np.array( [xx1.ravel(), xx2.ravel()]).T =%s" % np.array( [xx1.ravel(), xx2.ravel()]).T)
    Z = classifier.predict(np.array( [xx1.ravel(), xx2.ravel()]).T)
    print("Z = %s" % Z)
    Z = Z.reshape(xx1.shape)
    print("Z.reshape(xx1.shape) = %s" % Z)

    plt.contourf(xx1,xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    
    for idx, cl in enumerate(np.unique(y)):
        print("idx=%s, cl=%s" % (idx,cl))
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)
    

def main():
    
    df = pd.read_csv('./sensor.data',header=None)
    df.tail();

    y = df.iloc[0:99, 2].values
    y = np.where(y == 'Abnormal', -1, 1)
    X = df.iloc[0:99, [0,1]].values

    ppn = Perceptron(eta=0.1, n_iter=10) 
    ppn.fit(X,y)
    '''    
    Weight=ppn.get_w();
    print("fit weight W = %s" % Weight)
   
    print("----------")
    X_point=np.array([5,3])
    predict=ppn.predict(X_point);
    print("X_point = %s, predict result = %d" % (X_point,predict))
    X_point=np.array([5,1])
    predict=ppn.predict(X_point);
    print("X_point = %s, predict result = %d" % (X_point,predict))
    '''

    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('Temperature (X1)')
    plt.ylabel('Humidity (X2)')
    plt.legend(loc='upper left')
    plt.show();        
   
 
print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
