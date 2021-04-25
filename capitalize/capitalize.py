#!/bin/python 



def solve(s):
    # Algo: 
    # split string on the space, save to splitStr list 
    # iterate through each item, call builtin capitalize 
    # Save to temp list t 
    # save string to list to string var ltos 

    t = []
    splitStr = s.split()
    for i in splitStr:
        t.append(i.capitalize())
        ltos = ' '.join(map(str, t))
    return ltos 

if __name__ == '__main__':
    s = str(input())

    result = solve(s) 

    print (result)
