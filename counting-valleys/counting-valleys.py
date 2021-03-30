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
    # cU = countUps
    # cD = countDowns
    cU = 0
    cD = 0
    for s in len(path):
        if s == "U":
            cU += 1
        if s == "D":
            cD += 1
    return int(cU - cD)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print (result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

