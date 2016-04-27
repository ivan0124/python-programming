#!/usr/bin/python

def main():
   
    #1 dimension 
    a = [1,2,3,4,5]
    print "list x =======>"
    for x in a:
        print x
    #
    sol=[ 2*x+3 for x in a if (2*x+3) < 10]
    print "2*x+3 < 10 list =======>"
    print sol

    #2 dimension
    a = [(1,2), (3,4),(9,8),(7,6),(5,4)]
    print "list (x,y) =======>"
    for x,y in a:
        print (x,y)
    #
    sol=[ x+y for x,y in a if (x+y) < 10]
    print "x+y < 10 list =======>"
    print sol
    
    #3 dimension
    a = [(1,2,-1), (3,4,10),(9,8,100),(7,6,-20),(5,4,-30)]
    print "list (x,y,z) =======>"
    for x,y,z in a:
        print (x,y,z)

    #


print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
