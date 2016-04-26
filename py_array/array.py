#!/usr/bin/python

import numpy as np

def main():
    a = np.array([1,2,3])
    print a[0], a[1], a[2]
    b = a
    print b[0], b[1], b[2]

    b[2] = 1000
    print a 
    print b


print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
