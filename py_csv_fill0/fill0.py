#!/usr/bin/python

import csv
import numpy as np
import pandas as pd

def main():

     with open("./hdd.csv","rb") as source:
	 rdr= csv.reader( source )
         #for row in rdr:
         #    for i, x in enumerate(row):
         #        if len(x)< 1:
         #            x = row[i] = 0
         #        print x
         with open("result.csv","wb") as result:
             wtr= csv.writer( result )
             for r in rdr:
                 for i, x in enumerate(r):
                     if len(x)< 1:
                         r[i] = 0
                 wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],r[8]) )
 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
