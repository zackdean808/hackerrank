#!/bin/python 

if __name__ == '__main__':
    append = "append" 
    insert = "insert" 
    sort = "sort" 
    pop = "pop" 
    reverse = "reverse" 
    remove = "remove"
    i = [] 
    tempList = [] 

    # Read in the times to run the foor loop 
    N = int(input())

    for i in range(0, N):
        line = str(input())

        if append in line:
            print ("appened") 
        elif insert in line:
            print ("insert") 
        elif sort in line:
            print ("sort") 
        elif pop in line:
            print ("pop") 
        elif reverse in line: 
            print ("reverse")
        elif remove in line:
            print ("remove") 
        elif "print" in line:
            print ("print") 
        else:
            print ("something went wrong")


