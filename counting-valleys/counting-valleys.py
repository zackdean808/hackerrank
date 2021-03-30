#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def countingValleys(steps, path):
    # Write your code here
    # cS = countSteps 
    # cV = countValleys 
    cS = 0
    cV = 0 
    for c in path:
        #print (c)
        if c == "U":
            cS += 1
            #print ("Up")
        if c == "D":
            cS -= 1
            #print ("Down")
        if cS == 0 and c == "U":
            cV += 1 
            #print("valley") 
    return int(cV)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print (result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

