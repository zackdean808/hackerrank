#!/bin/python 

import re 


def solve(s): 
    pattern = "^[789][0-9]{9}$"
    if re.match(pattern, s):
        return "YES"
    elif not re.match(pattern, s):
        return "NO"
    else:
        sys.exit(1)

if __name__ == '__main__':
    N = int(input())
    for i in range(0, N):
        s = str(input())
        result = solve(s) 
        print (result)
