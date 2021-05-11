#!/bin/python 

if __name__ == '__main__':
    append = "append"
    insert = "insert"
    sort = "sort"
    pop = "pop"
    reverse = "reverse"
    remove = "remove"
    l = []
    tempList = []

    # Read in the times to run the foor loop 
    N = int(input())

    for i in range(0, N):
        line = str(input())

        if append in line:
            #print ("appened")
            # Bug by getting string -1, this did not get double digits 
            # Just grabbed the last element in the split string cast as int 
            # then append 
            tempList = line.split()
            l.append(int(tempList[-1]))
            tempList.clear()
        elif insert in line:
            #print ("insert") 
            tempList = line.split()
            l.insert(int(tempList[1]),int(tempList[2]))
            tempList.clear()
            #change this to  a split and use that. 
        elif sort in line:
            #print ("sort")
            l.sort()
        elif pop in line:
            #print ("pop") 
            l.pop(-1)
        elif reverse in line:
           # print ("reverse")
           l.reverse()
        elif remove in line:
            #print ("remove")
            l.remove(int(line[-1]))
        elif "print" in line:
            #print ("print")
            print (l)
        else:
            print ("something went wrong")
