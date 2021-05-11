#!/bin/python 

if __name__ == '__main__':
    
    discard = "discard" 
    pop = "pop"
    remove = "remove"
    
    # Read in the length of the set
    numberOfItems = int(input())
    # Read in the set and discard any space/newline char 
    s = set(map(int, input().split()))
    s.discard(' ')
    # Read in the times to run the foor loop 
    numberOfCommands = int(input())
    total = 0 
    
    for i in range(0, numberOfCommands):
        line = str(input())
        line.strip()
        if discard in line:
            #print ("pop") 
            s.discard(int(line[-1]))
        elif remove in line:
            #print ("remove")
            try:
                s.remove(int(line[-1]))
            except:
                pass 
        elif pop in line:
            s.pop()
        else:
            print ("something went wrong")

    for i in s:
        total += i

    print(total) 
