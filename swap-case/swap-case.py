#!/bin/python
def swap_case(s):
    #it was that easy according to the docs :| 
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
