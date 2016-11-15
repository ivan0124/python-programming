#!/usr/bin/python

import csv
import numpy as np
import pandas as pd

def main():

     with open("./gg.csv","rb") as source:
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
                 wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7],r[8],r[9],
                                r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17],r[18],r[19],
                                r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27],r[28],r[29],
                                r[30], r[31], r[32], r[33], r[34], r[35], r[36], r[37],r[38],r[39],
                                r[40], r[41], r[42], r[43], r[44], r[45], r[46], r[47],r[48],r[49],
                                r[50], r[51], r[52], r[53], r[54], r[55], r[56], r[57],r[58],r[59],
                                r[60], r[61], r[62], r[63], r[64], r[65], r[66], r[67],r[68],r[69],
                                r[70], r[71], r[72], r[73], r[74], r[75], r[76], r[77],r[78],r[79],
                                r[80], r[81], r[82], r[83], r[84], r[85], r[86], r[87],r[88],r[89]
                               ) )
 

print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
