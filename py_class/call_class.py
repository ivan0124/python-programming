#!/usr/bin/python

import library as lib

def main():
    print ("Hello, Class!")

    #call class
    a = lib.Animal("dog",10, 2)
    print "The name is " +  a.who()
    print "The weight x height = %s" % a.wxh()

print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
