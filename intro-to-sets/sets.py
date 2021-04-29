#!/bin/python

def average(array):
    # your code goes here
    mySet = set(array)
    length = len(mySet)
    total = 0 
    for i in mySet:
        total += i
    return (total/length)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
