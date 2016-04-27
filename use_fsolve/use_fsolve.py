#!/usr/bin/python

from scipy.optimize import fsolve

def f(x):
    return 3*x+1

def main():

    x = fsolve(f,1)
    print x
   
print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
