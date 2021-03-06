#!/usr/bin/python

import numpy as np
import configparser

class Perceptron(object):

   def __init__(self, eta=0.01, n_iter=10):
      self.eta = eta
      self.n_iter = n_iter
   
   def fit(self, X, y):
      self.w_ = np.zeros(1 + X.shape[1])
      self.errors_ = []
  
      for _ in range(self.n_iter):
          errors = 0
          for xi, target in zip(X,y):
              update = self.eta * (target - self.predict(xi))
              self.w_[1:] += update * xi
              self.w_[0] += update
              errors += int(update != 0.0)
          self.errors_.append(errors)
      return self

   def net_input(self, X):
       return np.dot(X, self.w_[1:]) + self.w_[0]

   def predict(self, X):
       return np.where(self.net_input(X) >= 0.0, 1, -1)

   def get_w(self):
       return self.w_

   def set_w(self, w):
       self.w_ = w

def set_weight(config_path_name):

    config = configparser.ConfigParser()
    config.read(config_path_name)
    print(config['DEFAULT']['weight'])
    a=config['DEFAULT']['weight']

    print("read FILE.INI weight =%s" % a)
    floats = map(float, a.split(','))

    print('------------');
    print("set perceptron weight  = %s" % floats)
    ppn.set_w( np.array(floats))
    Weight=ppn.get_w();
    print("get perceptron weight  = %s" % Weight)
    print("----------")
    return 0

def predict(X):
    print("predict")
    print("----------")
    floats = map(float, X.split(','))
    X_point=np.array(floats)
    predict=ppn.predict(X_point);
    print("X_point = %s, predict result = %d" % (X_point,predict))
    return predict


def main():
    print ("Hello, pla.py main() run!")
    set_weight("FILE.INI")
    predict("5,3")
 
print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    ppn = Perceptron(eta=0.3, n_iter=10)
    main()
else:
    print("pla.py is loaded.");
    ppn = Perceptron(eta=0.3, n_iter=10)
