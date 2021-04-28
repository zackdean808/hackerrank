#!/bin/python 

import re

def solve(s):
    pattern = "\<[a-zA-Z]{1,}[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}\>"
    tempStr = s.split()
    if re.match(pattern, tempStr[1]):
        print (tempStr[0], tempStr[1])
        tempStr.clear()

if __name__ == '__main__':
    
    N = int(input())

    for i in range(0, N):
        inputString = str(input())
        solve(inputString)

