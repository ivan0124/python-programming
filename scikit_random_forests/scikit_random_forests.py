#!/usr/bin/python

import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02): 
    markers = ['s', 'x', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'gary', 'cyan']
    cmap = ListedColormap(colors[:len(np.unique(y))])

    #plot the decision surface
    x1_min, x1_max = X[:, 0].min()-1, X[:, 0].max()+1
    x2_min, x2_max = X[:, 1].min()-1, X[:, 1].max()+1

    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), 
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array( [xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1,xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    #plot all sample 
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

    #highlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:,0], X_test[:, 1], c='',
                    alpha=1.0, linewidth=1, marker='o',
                    s=55, label='test set')
 

def main():

    #import data
    iris = datasets.load_iris()
    X = iris.data[:,[2,3]]
    y = iris.target

    #cross_validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    #print (X_train) 

    #standardize the feature
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train) 
    X_test_std = sc.transform(X_test)
   
    #trainning model
    forest = RandomForestClassifier(criterion='entropy', 
                                    n_estimators=10, 
                                    random_state=1,
                                    n_jobs=2)
    forest.fit(X_train, y_train) 

    #predict
    y_pred = forest.predict(X_test);
    print("Misclassified samples: %d" %(y_test != y_pred).sum()) 
    
    #Accuracy
    print(y_test)
    print(y_pred)
    print("Accuracy: %.2f" % accuracy_score(y_test, y_pred))

    #
    X_combined = np.vstack((X_train, X_test)) 
    y_combined = np.hstack((y_train, y_test))
    plot_decision_regions(X=X_combined,
                          y=y_combined,
                          classifier=forest,
                          test_idx=range(105,150))
    plt.xlabel('petal length [cm]')
    plt.ylabel('petal width [cm]')
    plt.legend(loc='upper left')
    plt.show()
 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
