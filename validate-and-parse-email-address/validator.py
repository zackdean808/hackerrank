#!/bin/python 

import re

def solve(s):
    pattern = re.compile("\<[a-zA-Z]{1,}[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}\>")
    t = s.split()
    print (t[1])
    if re.match(pattern, t[1]):
        return "YES"
        print ("YES")
        print (t[1])
    elif not re.match(pattern, t[1]):
        return "NO"
        print ("NO")
        print (t[1])
    else:
        sys.exit(1)
    t.clear()

if __name__ == '__main__':
    N = int(input())
    for i in range(0, N):
        s = str(input())

        result = solve(s)
        print (result)

