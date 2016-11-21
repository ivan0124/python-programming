#!/usr/bin/python

def main():

    my_y = [[1, 2, 3], 
            [1, 3, 2]]

    for i in range(len(my_y)):
        my_y[i] = map( lambda x : x*x if x>2 else x*0, my_y[i] )

    print ("map my_y = %s \n" % my_y)

    ############################
    #x-> x*x, input=[1,2,3] --> output=[1,4,9]
    my_y1 = [1, 2, 3]
    my_y1 = map( lambda x : x*x, my_y1 )
    print ("map my_y1 = %s \n" % my_y1)


if __name__  == "__main__":
    main()
