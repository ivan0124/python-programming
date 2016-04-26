#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():

    x = np.arange(0,180)
    y = np.sin(x * np.pi / 180.0)

    #input x,y list for drawing
    plt.plot(x,y) 

    # set plot range
    plt.xlim(-30,390)
    plt.ylim(-1.5,1.5)

    # set x, y label and title
    plt.xlabel("x-axis") 
    plt.ylabel("y-axis") 
    plt.title("The Title") 

    #show picture
    plt.show() 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
