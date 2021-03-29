#!/bin/python
import re 

def count_substring(string, sub_string):
    count = 0 
    left = 0 
    while True:
        match = re.search(string, sub_string)
        if not match:
            break
        count += 1
        left += match.start() + 1
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
