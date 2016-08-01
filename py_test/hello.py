#!/usr/bin/python

import pandas as pd

def main():
    print ("Hello, World!")
    df = pd.read_csv('./iris.data',header=None)

print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
