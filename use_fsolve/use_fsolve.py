#!/usr/bin/python

from scipy.optimize import fsolve

def f(x):
    return x**2-25

def main():

    x = fsolve(f,3)
    print x
   
print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
