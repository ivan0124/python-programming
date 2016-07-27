#!/usr/bin/python

import library as lib

def main():
    print ("Hello, World!")

    #input is nubmer
    res=lib.funA(10,5)
    print ("res number=%d" % (res))
    
    #input is string
    res=foo("777","333")
    print ("res string=%s" % (res))

    for i in range(1,10):
        print ("i=%d" % i)

def foo(p1, p2):
    res=p1+p2
    return res

print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
