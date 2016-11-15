#!/usr/bin/python

import csv
import numpy as np
import pandas as pd


def main():

    with open("./result.csv","rb") as source:
        rdr= csv.reader( source )
        with open("smart.csv","wb") as result:
            wtr= csv.writer( result )
            for r in rdr:
                wtr.writerow( (r[4], r[6], r[10], r[12], r[14], r[16], r[20], r[22], r[26], r[38], 
                               r[46], r[48], r[50], r[52], r[58], r[60], r[62]) )
 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
