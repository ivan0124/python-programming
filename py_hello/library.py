#!/usr/bin/python

def main():
    print ("library.py running!")

def funA(p1, p2):
    res=p1+p2
    return res

print ("__name__ value is %s" % (__name__))

if __name__  == "__main__":
    main()
else:
    print ("library.py running as module")
