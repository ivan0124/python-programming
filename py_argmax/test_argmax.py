#!/usr/bin/python

import numpy as np

def main():

    my_y = [[1, 2, 3], 
            [4, 5, 1]]

    # index [1, 1, 0] --> value [4, 5, 3]
    my_y0 = np.argmax(my_y, axis=0) 
    print ("map my_y0 = %s \n" % my_y0)

    # index [2, 1] --> value [3, 5]
    my_y1 = np.argmax(my_y, axis=1) 
    print ("map my_y1 = %s \n" % my_y1)

if __name__  == "__main__":
    main()
