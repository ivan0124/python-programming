#!/usr/bin/python

from sympy.abc import x, y

def main():
    e=x+y+x
    print e


print "__name__ value is %s" % (__name__)

if __name__  == "__main__":
    main()
