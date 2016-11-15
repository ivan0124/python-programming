#!/usr/bin/python

import csv
import numpy as np
import pandas as pd

def main():

    with open("./HDD_S.csv","rb") as source:
        rdr= csv.reader( source )
        with open("result.csv","wb") as result:
            wtr= csv.writer( result )
            for r in rdr:
                wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16]) )
 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
