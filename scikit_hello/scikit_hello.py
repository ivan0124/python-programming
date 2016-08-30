#!/usr/bin/python

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

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
   
    # 
     

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
