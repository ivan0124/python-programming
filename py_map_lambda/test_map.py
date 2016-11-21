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

    ############################
    my_y2 = [[0.7, 0.2], [0.1,0.8], [0.6, 0.4]]

    for i in range(len(my_y2)):
        if my_y2[i][0] > 0.618:
            my_y2[i][0] = 1
            my_y2[i][1] = 0
        else:
            my_y2[i][0] = 0
            my_y2[i][1] = 1

    print ("map my_y2 = %s \n" % my_y2)

if __name__  == "__main__":
    main()
