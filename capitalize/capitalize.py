#!/bin/python 

def solve(s):
    t = []
    splitStr = s.split()
    for i in splitStr:
        #print (i.capitalize())
        #t.append(i.capitalize())
        t.append(i)

    return s.join(t) 

if __name__ == '__main__':
    s = str(input())

    result = solve(s) 

    print (result)
