#!/bin/python

if __name__ == '__main__':
    n = int(input())
    # Convert the map to a list so it's easier to work with
    arr = list(map(int, input().split()))
    
    # sort the array in ascending order 
    arr.sort(key = lambda x: x)
    # Reverse the array so it's in desending order
    arr.reverse()

    i = 0
    while i < n:
        if arr[i] == arr[i + 1]:
            i+=1
        elif arr[i] > arr[i + 1]:
            print (arr[i + 1])
            break
        else:
            i+=1
