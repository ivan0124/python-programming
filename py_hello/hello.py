#!/usr/bin/python

def main():
    print "Hello, World!"

    #input is nubmer
    res=foo(10,5)
    print "res number=%d" % (res)
    
    #input is string
    res=foo("777","333")
    print "res string=%s" % (res)

def foo(p1, p2):
    res=p1+p2
    return res

if __name__  == "__main__":
    main()
